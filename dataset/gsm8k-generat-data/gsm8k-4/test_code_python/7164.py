def solution():
    """James' keyboard is missing 1/7 of the consonants and two vowels. How many keys are missing in total? (Remember there are 5 vowels and 21 consonants in the alphabet.)"""
    # Define the number of vowels and consonants in the alphabet
    num_vowels = 5
    num_consonants = 21

    # Calculate the number of missing consonants and vowels
    missing_consonants = num_consonants / 7
    missing_vowels = 2

    # Calculate the total number of missing keys
    total_missing_keys = missing_consonants + missing_vowels

    # return the result
    result = total_missing_keys
    return result

print(solution())