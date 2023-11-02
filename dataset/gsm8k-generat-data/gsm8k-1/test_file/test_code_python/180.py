def solution():
    """Jerry is rolling a six-sided die. How much more likely is it (expressed as a percentage) that he rolls a number greater than 3 than that he rolls two even numbers in a row?"""
    total_outcomes = 6
    greater_than_3_outcomes = 2
    even_outcomes = 3
    even_in_a_row_outcomes = 1
    probability_greater_than_3 = greater_than_3_outcomes / total_outcomes
    probability_even_in_a_row = (even_outcomes / total_outcomes) * (even_outcomes / total_outcomes)
    difference = probability_greater_than_3 - probability_even_in_a_row
    percentage_difference = difference * 100
    result = percentage_difference
    return result

print(solution())