def solution():
    """Trisha needed to buy some groceries for herself and her dog. She spent $17 on meat, $22 on chicken, $43 on all the veggies, $5 on the eggs, and finally $45 on her dog’s food. When she left the store, she had only $35 left. How much money did she bring with her at the beginning?"""
    # Define the total cost of the groceries
    total_cost = 17 + 22 + 43 + 5 + 45

    # Define the remaining amount of money
    remaining_money = 35

    # Calculate the initial amount of money Trisha had
    initial_money = total_cost + remaining_money

    result = initial_money
    return result

print(solution())