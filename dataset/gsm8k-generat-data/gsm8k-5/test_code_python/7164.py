def solution():
    total_vowels = 5  # There are 5 vowels in the alphabet
    total_consonants = 21  # There are 21 consonants in the alphabet

    # Calculate the number of missing consonants
    missing_consonants = total_consonants / 7

    # Calculate the total number of missing keys
    total_missing = missing_consonants + 2

    result = total_missing
    return result

print(solution())