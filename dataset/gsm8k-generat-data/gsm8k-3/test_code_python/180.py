def solution():
    """Derek has $960 to buy his books for the semester. He spends half of that on his textbooks, and he spends a quarter of what is left on his school supplies. What is the amount of money Derek has left?"""
    # Define the initial amount of money Derek has
    initial_amount = 960

    # Calculate the amount spent on textbooks
    textbooks_cost = initial_amount / 2

    # Calculate the remaining amount of money
    remaining_amount = initial_amount - textbooks_cost

    # Calculate the amount spent on school supplies
    supplies_cost = remaining_amount / 4

    # Calculate the final amount of money Derek has left
    final_amount = remaining_amount - supplies_cost

    result = final_amount
    return result

print(solution())