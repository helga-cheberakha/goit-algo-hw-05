import timeit
from collections.abc import Callable
from pathlib import Path

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def read_file(filename: str) -> str:
    path = Path(__file__).parent / filename
    with path.open("r", encoding="utf-8") as file:
        return file.read()

def benchmark(func: Callable, text: str, pattern: str) -> float:
    timings = timeit.repeat(lambda: func(text, pattern), number=100, repeat=5)
    return min(timings) / 100

def get_fastest(label: str, totals: dict[str, float]) -> None:
    """ 
    Print the algorithm with the lowest sum of the search time
    for real and fake patterns.
    """
    fastest_time = min(totals.values())
    algorithms = [name for name, seconds in totals.items() if seconds == fastest_time]
    print(f"{label}: {', '.join(algorithms)} ({fastest_time:.9f}s combined)")

def main() -> None:
    articles = {
        "article1.txt": "Жадібний алгоритм",
        "article2.txt": "хеш-таблиця",
    }
    algorithms = (boyer_moore_search, kmp_search, rabin_karp_search)
    fake_pattern = "Lorem ipsum dolor"

    texts = {article_name: read_file(f"files/{article_name}") for article_name in articles}
    article_totals: dict[tuple[str, str], float] = {}

    print(f"| {'Algorithm':<24} | {'Pattern':<8} | {'Article':<15}  | {'Seconds':>14}")

    for algorithm in algorithms:
        algorithm_name = algorithm.__name__

        for pattern_type in ("real", "fake"):
            for article_name, real_pattern in articles.items():
                pattern = real_pattern if pattern_type == "real" else fake_pattern
                seconds = benchmark(algorithm, texts[article_name], pattern)

                print(f"| {algorithm_name:<24} | {pattern_type:<8} | {article_name:<15} | {seconds:>14.9f}")

                key = (article_name, algorithm_name)
                article_totals[key] = article_totals.get(key, 0.0) + seconds

        print()

    print("Fastest by combined search time for real and fake patterns")

    for article_name in articles:
        totals = {}
        for algorithm in algorithms:
            algorithm_name = algorithm.__name__
            totals[algorithm_name] = article_totals[article_name, algorithm_name]

        get_fastest(article_name, totals)

    overall_totals = {}
    for algorithm in algorithms:
        algorithm_name = algorithm.__name__
        total = 0.0
        for article_name in articles:
            total += article_totals[article_name, algorithm_name]

        overall_totals[algorithm_name] = total

    get_fastest("Overall", overall_totals)

if __name__ == "__main__":
    main()
