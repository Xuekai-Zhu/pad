def solution():
    # Calculate the cost of 5 pansies
    pansy_cost = 5 * 2.5

    # Calculate the cost of 5 petunias
    petunia_cost = 5

    # Calculate the total cost before discount
    total_cost = pansy_cost + petunia_cost + 12.5

    # Calculate the discount amount
    discount = total_cost * 0.1

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    # Calculate the change from $50 bill
    change = 50 - total_cost_after_discount
    result = change
    return result

print(solution())