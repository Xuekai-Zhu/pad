def solution():
    # Calculate the total amount Gerald needs to save for baseball supplies
    total_cost = 100 * 4  # he spends $100 a month and his season is 4 months long

    # Calculate the amount Gerald can earn from doing chores in the remaining months
    total_earnings = total_cost / 2  # he has 4 months of baseball and 4 months of doing chores

    # Calculate the average number of chores he needs to do per month
    chores_per_month = total_earnings / 10  # he charges $10 for each chore

    result = chores_per_month
    return result

print(solution())