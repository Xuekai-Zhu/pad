def solution():
    """ Derek has $960 to buy his books for the semester. He spends half of that on his textbooks, and he spends a quarter of what is left on his school supplies. What is the amount of money Derek has left? """
    # Define the initial amount of money
    initial_money = 960

    # Calculate the amount spent on textbooks
    textbook_cost = initial_money / 2

    # Calculate the amount of money left after purchasing textbooks
    remaining_money = initial_money - textbook_cost

    # Calculate the amount spent on school supplies
    supplies_cost = remaining_money / 4

    # Calculate the amount of money left after purchasing school supplies
    final_money = remaining_money - supplies_cost

    result = final_money
    return result

print(solution())