def solution():
    roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]
    before_H = roman_numerals.index("G") + 1
    after_H = roman_numerals.index("I") - 1
    missing_letters = []
    for i in range(before_H, after_H):
        if roman_numerals[i] not in ["H", "G", "I"]:
            missing_letters.append(roman_numerals[i])
    if missing_letters:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())