def solution():
    days_left = 3  # Jackson has 3 days left in the week
    remaining_goal = 1000 - 300 - 40  # Jackson still needs to collect this much money to meet his goal
    money_per_house = 10 / 4  # Jackson earns $2.50 per house

    # Calculate the total number of houses Jackson needs to visit to meet his goal
    houses_needed = remaining_goal / money_per_house

    # Calculate the average number of houses Jackson needs to visit per remaining day
    houses_per_day = houses_needed / days_left
    result = houses_per_day
    return result

print(solution())