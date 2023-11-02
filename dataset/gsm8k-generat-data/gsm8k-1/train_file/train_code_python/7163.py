def solution():
    """James' keyboard is missing 1/7 of the consonants and two vowels. How many keys are missing in total? (Remember there are 5 vowels and 21 consonants in the alphabet.)"""
    vowels = 5
    consonants = 21
    missing_consonants = consonants//7
    missing_vowels = 2
    total_missing_keys = missing_consonants + missing_vowels
    result = total_missing_keys
    return result

print(solution())