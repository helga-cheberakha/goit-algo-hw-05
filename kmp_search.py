def compute_lps(pattern: str) -> list:
    """ Build the longest proper prefix-suffix table. """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # The current character extends the matching prefix.
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Try a shorter prefix with the same character.
                length = lps[length - 1]
            else:
                # No prefix matches here, lps[i] is zero.
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string: str, pattern: str) -> int:
    """ 
    Return the index of the first match,
    or -1 if the pattern is not found. 
    """
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    # i tracks the text position.
    # j counts the matched pattern characters.
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            # No characters are matched, move to the next text character.
            i += 1

        if j == M:
            return i - j

    return -1
