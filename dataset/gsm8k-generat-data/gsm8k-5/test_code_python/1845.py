def solution():
    # Calculate the cost of buying 4 CDs of each type
    rock_cost = 5 * 4
    pop_cost = 10 * 4
    dance_cost = 3 * 4
    country_cost = 7 * 4

    total_cost = rock_cost + pop_cost + dance_cost + country_cost

    # Calculate how much Julia is short
    short_amount = total_cost - 75
    result = short_amount
    return result

print(solution())