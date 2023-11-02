def solution():
    """On a shopping trip in a crowded store, Josie had to wait 3 minutes for a cart, 13 minutes for an employee to unlock a cabinet to get her a product, 14 minutes for a stocker to restock a shelf with what she wanted, and 18 minutes in line to check out. Her shopping trip took an hour and a half. How many minutes did Josie spend shopping instead of waiting?"""
    # Define the time Josie spent waiting
    wait_time = 3 + 13 + 14 + 18

    # Define the total shopping trip time in minutes
    trip_time = 90

    # Calculate the time Josie spent shopping
    shopping_time = trip_time - wait_time

    # Display the time Josie spent shopping instead of waiting
    result = shopping_time
    return result

print(solution())