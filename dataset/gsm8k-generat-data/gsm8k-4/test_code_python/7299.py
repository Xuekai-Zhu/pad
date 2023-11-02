def solution():
    """In the fall, a tree drops a tenth of its initial quantity of leaves each day over the course of four days, then abruptly drops the rest on the fifth day. If it had 340 leaves before they started to fall, how many leaves does it drop on the fifth day?"""
    # Define the initial quantity of leaves
    initial_leaves = 340

    # Define the quantity of leaves dropped each day for the first four days
    daily_drop = initial_leaves / 10 / 4

    # Calculate the total quantity of leaves dropped in the first four days
    first_four_days = daily_drop * 4

    # Calculate the quantity of leaves dropped on the fifth day
    fifth_day = initial_leaves - first_four_days

    # Return the result
    result = fifth_day
    return result

print(solution())