def solution():
    initial_fee = 80
    fee_increase = 10
    number_of_years = 6
    total_fee = ((fee_increase * number_of_years) + initial_fee)
    result = total_fee
    return result

print(solution())