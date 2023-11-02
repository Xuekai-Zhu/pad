def solution():
    sunday_drinking = 2
    monday_drinking = 4
    daily_drinking = 3
    num_days = 6 # Monday to Saturday, excluding Sunday

    # Calculate the total number of glasses of water Rachel drinks in a week
    total_glasses = sunday_drinking + monday_drinking + (daily_drinking * num_days)

    # Calculate the total ounces of water Rachel drinks in a week
    total_ounces = total_glasses * 10

    # Calculate how many more ounces of water Rachel needs to drink on Saturday
    remaining_ounces = 220 - total_ounces

    # Calculate how many glasses of water Rachel needs to drink on Saturday
    saturday_glasses = remaining_ounces / 10
    result = saturday_glasses
    return result

print(solution())