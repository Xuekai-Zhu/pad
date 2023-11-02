def solution():
    # Calculate the base score of the word
    base_score = 30 / 3

    # Calculate the value of the first and third letters
    first_and_third_value = 1 + 1

    # Calculate the total value of the middle letter
    middle_value = base_score - first_and_third_value
    result = middle_value
    return result

print(solution())