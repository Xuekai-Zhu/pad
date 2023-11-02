def solution():
    """In the fall, a tree drops a tenth of its initial quantity of leaves each day over the course of four days, then abruptly drops the rest on the fifth day. If it had 340 leaves before they started to fall, how many leaves does it drop on the fifth day?"""
    # Define the initial number of leaves and the daily decrease rate
    initial_leaves = 340
    daily_decrease_rate = initial_leaves / 10

    # Calculate the number of leaves dropped each day for the first four days
    day1_leaves_dropped = daily_decrease_rate
    day2_leaves_dropped = daily_decrease_rate * 2
    day3_leaves_dropped = daily_decrease_rate * 3
    day4_leaves_dropped = daily_decrease_rate * 4

    # Calculate the total number of leaves dropped in the first four days
    leaves_dropped_first_four_days = day1_leaves_dropped + day2_leaves_dropped + day3_leaves_dropped + day4_leaves_dropped

    # Calculate the number of leaves dropped on the fifth day
    leaves_dropped_fifth_day = initial_leaves - leaves_dropped_first_four_days

    # Display the number of leaves dropped on the fifth day
    result = leaves_dropped_fifth_day
    return result

print(solution())