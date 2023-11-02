def solution():
    # Calculate the cost of the hummus
    hummus_cost = 2 * 5

    # Calculate the total cost of the other items
    other_items_cost = 20 + 10 + 10

    # Calculate the total amount spent
    total_spent = hummus_cost + other_items_cost

    # Calculate the remaining amount
    remaining_amount = 60 - total_spent

    # Calculate the number of apples that can be purchased with the remaining amount
    apples_cost = 2
    number_of_apples = remaining_amount // apples_cost
    result = number_of_apples
    return result

print(solution())