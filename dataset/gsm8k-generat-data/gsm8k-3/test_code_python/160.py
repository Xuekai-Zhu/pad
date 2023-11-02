def solution():
    """John throws a block party and splits the cost with 3 other people. They buy 100 pounds of burgers at $3 per pound. They also buy $80 of condiments and propane to cook everything. John also buys all the alcohol which costs $200. How much did John spend altogether"""
    # Define the cost of the burgers, condiments/propane, and alcohol
    burger_cost = 100 * 3
    condiments_cost = 80
    alcohol_cost = 200

    # Calculate the total cost and the cost split across 4 people
    total_cost = burger_cost + condiments_cost + alcohol_cost
    cost_per_person = total_cost / 4

    # Calculate John's total spending
    john_spending = cost_per_person - (burger_cost / 4)

    result = john_spending
    return result

print(solution())