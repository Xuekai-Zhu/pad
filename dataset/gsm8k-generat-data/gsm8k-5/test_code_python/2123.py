def solution():
    # Calculate the total cost of the items Bruce bought
    crayons_cost = 5 * 5
    books_cost = 10 * 5
    calculators_cost = 3 * 5
    total_cost = crayons_cost + books_cost + calculators_cost

    # Calculate the change he gets from $200
    change = 200 - total_cost

    # Calculate the number of bags he can buy with the change
    bags_can_buy = change // 10
    result = bags_can_buy
    return result

print(solution())