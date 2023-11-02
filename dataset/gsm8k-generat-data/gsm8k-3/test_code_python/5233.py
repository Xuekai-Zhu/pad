def solution():
    """Trisha needed to buy some groceries for herself and her dog. She spent $17 on meat, $22 on chicken, $43 on all the veggies, $5 on the eggs, and finally $45 on her dog’s food. When she left the store, she had only $35 left. How much money did she bring with her at the beginning?"""
    # Define the expenses for each item
    meat_cost = 17
    chicken_cost = 22
    veggie_cost = 43
    egg_cost = 5
    dog_food_cost = 45

    # Calculate the total expenses
    total_expenses = meat_cost + chicken_cost + veggie_cost + egg_cost + dog_food_cost

    # Calculate the initial amount of money Trisha brought with her
    initial_amount = total_expenses + 35

    # Display the initial amount
    result = initial_amount
    return result

print(solution())