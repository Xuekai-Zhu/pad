def solution():
    """James' keyboard is missing 1/7 of the consonants and two vowels. How many keys are missing in total? (Remember there are 5 vowels and 21 consonants in the alphabet.)"""
    # Define the number of vowels and consonants in the alphabet
    VOWELS = 5
    CONSONANTS = 21

    # Calculate the number of missing consonants
    missing_consonants = CONSONANTS // 7

    # Calculate the total number of missing keys
    total_missing = missing_consonants + 2

    # Display the total number of missing keys
    result = total_missing
    return result

print(solution())