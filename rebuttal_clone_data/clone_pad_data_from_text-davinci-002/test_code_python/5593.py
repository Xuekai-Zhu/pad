def solution():
    initial_lumber = 450
    initial_nails = 30
    initial_fabric = 80
    inflation_rate_lumber = 20
    inflation_rate_nails = 10
    inflation_rate_fabric = 5
    new_lumber = initial_lumber * (1 + (inflation_rate_lumber / 100))
    new_nails = initial_nails * (1 + (inflation_rate_nails / 100))
    new_fabric = initial_fabric * (1 + (inflation_rate_fabric / 100))
    total_change = new_lumber + new_nails + new_fabric - (initial_lumber + initial_nails + initial_fabric)
    result = total_change
    return result

print(solution())