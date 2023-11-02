def solution():
    baseball_supplies = 100  # Gerald spends $100 a month on baseball supplies
    season_length = 4  # Gerald's baseball season is 4 months long
    non_season_months = 12 - season_length  # Gerald has to save up during the non-season months

    # Calculate the total amount Gerald needs to save up during the non-season months
    total_savings_needed = baseball_supplies * non_season_months

    # Calculate the number of chores Gerald needs to do each month to save up for his supplies
    chores_per_month = total_savings_needed / 10
    result = chores_per_month
    return result

print(solution())