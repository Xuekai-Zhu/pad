def solution():
    # Calculate the cost of each item Ray purchased
    hamburger_meat = 5.00
    crackers = 3.50
    frozen_vegetables = 2.00 * 4
    cheese = 3.50

    # Calculate the total cost of Ray's groceries
    total_cost = hamburger_meat + crackers + frozen_vegetables + cheese

    # Calculate Ray's discount as a rewards member
    discount = total_cost * 0.1

    # Calculate Ray's final total after the discount is applied
    final_total = total_cost - discount
    result = final_total
    return result

print(solution())