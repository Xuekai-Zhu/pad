def solution():
    
    initial_investment = 20 * 15
    increased_value = (2 / 3) * 15
    new_value = 15 + increased_value
    number_of_coins_sold = initial_investment / new_value
    result = number_of_coins_sold
    return result

print(solution())