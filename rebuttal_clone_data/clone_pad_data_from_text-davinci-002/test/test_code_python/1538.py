def solution():
    initial_score = 30
    tripled_score = initial_score / 3
    first_and_third_letters = 2
    middle_letter = tripled_score - first_and_third_letters
    result = middle_letter
    return result

print(solution())