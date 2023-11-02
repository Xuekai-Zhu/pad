def solution():
    """Gerald spends $100 a month on baseball supplies. His season is 4 months long. He wants to use the months he's not playing baseball to save up by raking, shoveling, and mowing lawns. He charges $10 for each. How many chores does he need to average a month to save up for his supplies?"""
    # Define the cost of baseball supplies and the number of months
    baseball_supplies = 100 * 4

    # Calculate the amount of money Gerald needs to save
    savings_needed = baseball_supplies - (100 * 4)

    # Calculate the number of chores Gerald needs to do to save up
    chores_needed = savings_needed / 10

    # Calculate the average number of chores needed per month
    months_offseason = 12 - 4
    chores_per_month = chores_needed / months_offseason

    # Round up to the nearest whole number of chores per month
    chores_per_month = int(chores_per_month) + 1

    result = chores_per_month
    return result

print(solution())