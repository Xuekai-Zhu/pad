def solution():
    """Gerald spends $100 a month on baseball supplies. His season is 4 months long. He wants to use the months he's not playing baseball to save up by raking, shoveling, and mowing lawns. He charges $10 for each. How many chores does he need to average a month to save up for his supplies?"""
    baseball_supplies = 100 * 4
    lawn_chore_cost = 10
    lawn_chore_months = 8
    chores_needed = baseball_supplies / (lawn_chore_cost * lawn_chore_months)
    result = chores_needed
    return result

print(solution())