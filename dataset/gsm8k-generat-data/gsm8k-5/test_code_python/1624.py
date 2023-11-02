def solution():
    pork_cost = 6 # the cost of pork per kilogram is $6
    chicken_cost = pork_cost - 2 # the cost of chicken per kilogram is $2 less than pork

    # calculate the cost of 1 kilogram of pork and 3 kilograms of chicken
    total_cost = (1 * pork_cost) + (3 * chicken_cost)
    result = total_cost
    return result

print(solution())