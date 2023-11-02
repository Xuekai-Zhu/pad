def solution():
    """On a shopping trip in a crowded store, Josie had to wait 3 minutes for a cart, 13 minutes for an employee to unlock a cabinet to get her a product, 14 minutes for a stocker to restock a shelf with what she wanted, and 18 minutes in line to check out. Her shopping trip took an hour and a half. How many minutes did Josie spend shopping instead of waiting?"""
    total_wait_time = 3 + 13 + 14 + 18
    total_time = 90
    shopping_time = total_time - total_wait_time
    result = shopping_time
    return result

print(solution())