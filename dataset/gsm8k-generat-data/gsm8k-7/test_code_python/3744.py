def solution():
    rum_on_pancakes = 10
    max_daily_rum = rum_on_pancakes * 3
    rum_consumed_today = 12

    # Calculate the remaining amount of rum Don can consume
    remaining_rum = max_daily_rum - rum_on_pancakes - rum_consumed_today
    result = remaining_rum
    return result

print(solution())