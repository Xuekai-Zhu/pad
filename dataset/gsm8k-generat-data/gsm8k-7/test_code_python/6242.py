def solution():
    num_bottles = 2
    bottle_size = 1.5  # in quarts
    additional_daily_ounces = 20

    # Find the total amount of water in the bottles
    total_bottle_water = num_bottles * bottle_size * 32  # convert quarts to ounces

    # Find the amount of additional water per day in ounces
    additional_daily_water = additional_daily_ounces

    # Find the total amount of additional water in a week in ounces
    additional_weekly_water = additional_daily_water * 7

    # Find the total amount of water consumed in a week
    total_weekly_water = total_bottle_water + additional_weekly_water

    # Convert the total amount of water to gallons
    total_weekly_gallons = total_weekly_water / 128

    result = total_weekly_gallons
    return result

print(solution())