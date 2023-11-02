def solution():
    original_investment = 400
    week_one_gain = original_investment * 0.25
    week_two_gain = (week_one_gain + original_investment) * 0.5
    current_value = original_investment + week_one_gain + week_two_gain
    result = current_value
    return result

print(solution())