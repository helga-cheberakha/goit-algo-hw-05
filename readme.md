# Execution times of search algorithms

| Algorithm | Pattern | Article | Seconds |
| :--- | --- | --- | ---: |
| boyer_moore_search | real | article1.txt | 0.000099392 |
| boyer_moore_search | real | article2.txt | 0.000012600 |
| boyer_moore_search | fake | article1.txt | 0.000096940 |
| boyer_moore_search | fake | article2.txt | 0.000143615 |
|     |     |     |     |
| kmp_search | real | article1.txt | 0.000572878 |
| kmp_search | real | article2.txt | 0.000040496 |
| kmp_search | fake | article1.txt | 0.000406955 |
| kmp_search | fake | article2.txt | 0.000603461 |
|     |     |     |     |
| rabin_karp_search | real | article1.txt | 0.001311431 |
| rabin_karp_search | real | article2.txt | 0.000088171 |
| rabin_karp_search | fake | article1.txt | 0.001290198 |
| rabin_karp_search | fake | article2.txt | 0.001895330 |

## Fastest algorithm by combined search time

| Scope | Fastest algorithm | Combined time |
| --- | --- | ---: |
| article1.txt | boyer_moore_search | 0.000196333 |
| article2.txt | boyer_moore_search | 0.000156215 |
|     |     |     |     |
| **Overall** | boyer_moore_search | **0.000352548** |