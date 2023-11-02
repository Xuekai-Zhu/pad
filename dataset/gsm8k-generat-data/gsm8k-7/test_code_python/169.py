def solution():
    current_grapes = 90
    yearly_grapes = current_grapes * 2  # 6 months to a year
    increase = 0.20 # 20% increase
    new_grapes = yearly_grapes * (1 + increase)
    result = new_grapes
    return result

print(solution())