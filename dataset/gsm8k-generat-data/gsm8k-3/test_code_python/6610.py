def solution():
    """In a week, Mortdecai collects 8 dozen  eggs every Tuesday and Thursday, and he delivers 3 dozen  eggs to the market and 5 dozen eggs to the mall. He then uses 4 dozen eggs to make a pie every Saturday. Mortdecai donates the remaining eggs to the charity by Sunday. How many eggs does he donate to the charity?"""
    # Define the number of dozens of eggs collected on Tuesday and Thursday
    eggs_collected = 8

    # Calculate the total number of dozens of eggs collected in a week
    total_eggs_collected = eggs_collected * 2

    # Subtract the dozens of eggs he delivers to the market and mall
    total_eggs_remaining = total_eggs_collected - 3 - 5

    # Subtract the dozens of eggs he uses to make a pie on Saturday
    total_eggs_remaining -= 4

    # Convert the total remaining dozens of eggs to the total number of eggs
    total_eggs_remaining *= 12

    # Display the number of eggs donated to charity
    result = total_eggs_remaining
    return result

print(solution())