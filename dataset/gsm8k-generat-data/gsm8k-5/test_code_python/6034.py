def solution():
    # Brendan caught 8 fish in the morning
    morning_catch = 8

    # Brendan threw 3 back that were too small
    morning_catch -= 3

    # Brendan caught 5 more in the afternoon
    afternoon_catch = 5

    # Brendan's total catch for the day
    brendan_total = morning_catch + afternoon_catch

    # Brendan's dad caught 13 fish
    dad_total = 13

    # Total number of fish caught
    total_catch = brendan_total + dad_total
    result = total_catch
    return result

print(solution())