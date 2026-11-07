def build_shift_table(pattern: str) -> dict:
    """ Build the shift table for the Boyer-Moore search. """
    table = {}
    length = len(pattern)

    # Store each character distance from the last position.
    # Skip the last position so all shifts are at least one.
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    
    # Use the full pattern length for the last character
    # if it does not appear earlier in the pattern.
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text: str, pattern: str) -> int:
    """ 
    Return the index of the first match,
    or -1 if the pattern is not found. 
    """
    shift_table = build_shift_table(pattern)
    i = 0

    # Keep searching while the full pattern fits
    # at the current position.
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        # Compare characters from right to left.
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        # If every character matches, return the start
        # of the match.
        if j < 0:
            return i

        # Choose the shift using the text character aligned with the last
        # character of the pattern. Use the full pattern length if the
        # text character is missing from the table.
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1
