def solution():
    """On a shopping trip in a crowded store, Josie had to wait 3 minutes for a cart, 13 minutes for an employee to unlock a cabinet to get her a product, 14 minutes for a stocker to restock a shelf with what she wanted, and 18 minutes in line to check out. Her shopping trip took an hour and a half. How many minutes did Josie spend shopping instead of waiting?"""
    # Define the total time spent on waiting
    total_waiting_time = 3 + 13 + 14 + 18

    # Define the total shopping time
    total_shopping_time = 90 - (total_waiting_time / 60)

    # Convert the total shopping time to minutes
    shopping_time_minutes = total_shopping_time * 60

    # Return the result
    result = shopping_time_minutes
    return result

print(solution())