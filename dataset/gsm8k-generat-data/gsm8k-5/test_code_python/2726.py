def solution():
    # The total score of the word after being tripled is 30
    total_score = 30

    # The first and third letters each have a value of 1, so their combined value is 2
    value_of_first_and_third_letters = 2

    # The score of the middle letter is equal to the total score minus the score of the first and third letters
    score_of_middle_letter = total_score - value_of_first_and_third_letters * 3  # 3 is the triple word score multiplier

    # The value of the middle letter is equal to its score
    value_of_middle_letter = score_of_middle_letter
    result = value_of_middle_letter
    return result

print(solution())