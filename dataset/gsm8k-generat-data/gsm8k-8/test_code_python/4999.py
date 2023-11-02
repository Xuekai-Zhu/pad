def solution():
    #Calculate the total cost of lollipops
    lollipop_cost = 4 * 1.50

    #Calculate the total cost of gummies
    gummies_cost = 2 * 2

    #Calculate the total cost of candies
    total_cost = lollipop_cost + gummies_cost

    #Calculate the amount left after spending on candies
    left_amount = 15 - total_cost

    result = left_amount
    return result

print(solution())