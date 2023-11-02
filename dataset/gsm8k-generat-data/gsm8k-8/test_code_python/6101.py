def solution():
    # Define the cost of the shoes and the savings so far
    shoe_cost = 120
    savings = 30

    # Calculate the amount he needs to save
    need_to_save = shoe_cost - savings

    # Calculate how much he can save each week
    weekly_savings = 5 * 3

    # Calculate how many weeks it will take to save enough
    weeks_to_save = need_to_save / weekly_savings

    # Round up to account for partial weeks
    weeks_to_save = math.ceil(weeks_to_save)
    result = weeks_to_save
    return result

print(solution())