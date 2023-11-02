def solution():
    days_until_birthday = 22
    flower_cost = 4
    daily_savings = 2

    # Calculate how much Lilly will save in total
    total_savings = days_until_birthday * daily_savings

    # Calculate how many flowers she can buy with her savings
    flowers = total_savings // flower_cost
    result = flowers
    return result

print(solution())