def solution():
    # Total number of consonants
    total_consonants = 21

    # Calculate the number of missing consonants
    missing_consonants = total_consonants / 7

    # Total number of vowels
    total_vowels = 5

    # Calculate the number of missing vowels
    missing_vowels = 2

    # Total number of missing keys
    total_missing_keys = missing_consonants + missing_vowels
    result = total_missing_keys
    return result

print(solution())