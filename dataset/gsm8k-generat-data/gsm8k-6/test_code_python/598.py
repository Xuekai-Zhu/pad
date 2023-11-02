def solution():
    # Calculate the minimum number of cups of vegetable Sarah needs to eat per day
    remaining_cups = 14 - 8  # Sarah needs to eat 14 cups of vegetables in a week (2 cups per day)
    days_remaining = 7 - 5  # Sunday to Thursday is 5 days, so there are 2 days remaining in the week
    cups_per_day = remaining_cups / days_remaining  # divide the remaining cups by the remaining days to get the minimum cups per day
    result = cups_per_day
    return result

print(solution())