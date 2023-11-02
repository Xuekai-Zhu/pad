def solution():
    english_vowels = ["A", "E", "I", "O", "U", "Y"]
    qwerty_first_line = ["E", "I", "O", "U", "Y"]
    vowel_count = 0
    for vowel in english_vowels:
        if vowel in qwerty_first_line:
            vowel_count += 1
    if vowel_count > len(english_vowels)/2:
        result = "Yes"
    else:
        result = "No"
    return result

print(solution())