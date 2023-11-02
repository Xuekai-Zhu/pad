def solution():
    # Calculate the number of missing consonants on James' keyboard
    missing_consonants = round(21/7)  # 1/7 of the consonants are missing

    # Calculate the number of missing vowels on James' keyboard
    missing_vowels = 2

    # Calculate the total number of missing keys on James' keyboard
    total_missing_keys = missing_consonants + missing_vowels
    result = total_missing_keys
    return result

print(solution())