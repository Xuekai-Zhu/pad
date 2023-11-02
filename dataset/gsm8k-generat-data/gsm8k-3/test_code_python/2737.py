def solution():
    """On Monday a group of 7 children and 5 adults went to the zoo. On Tuesday a group of 4 children and 2 adults went as well. Child tickets cost $3, and adult tickets cost $4. How much money did the zoo make in total for both days?"""
    # Define the ticket prices
    CHILD_PRICE = 3
    ADULT_PRICE = 4

    # Calculate the total revenue from Monday's group
    monday_revenue = 7 * CHILD_PRICE + 5 * ADULT_PRICE

    # Calculate the total revenue from Tuesday's group
    tuesday_revenue = 4 * CHILD_PRICE + 2 * ADULT_PRICE

    # Calculate the total revenue from both days
    total_revenue = monday_revenue + tuesday_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())