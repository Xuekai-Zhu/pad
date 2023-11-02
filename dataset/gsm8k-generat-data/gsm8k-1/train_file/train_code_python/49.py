def solution():
    """Gerald spends $100 a month on baseball supplies. His season is 4 months long. He wants to use the months he's not playing baseball to save up by raking, shoveling, and mowing lawns. He charges $10 for each. How many chores does he need to average a month to save up for his supplies?"""
    baseball_expenses = 100 * 4
    non_baseball_months = 12 - 4
    savings_needed = baseball_expenses / non_baseball_months
    chores_needed = savings_needed / 10
    result = chores_needed
    return result

print(solution())