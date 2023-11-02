def solution():
    most_common_letter_pair = "TH"
    free_letters = ["R", "S", "T", "L", "N", "E"]
    if most_common_letter_pair[1] in free_letters:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())