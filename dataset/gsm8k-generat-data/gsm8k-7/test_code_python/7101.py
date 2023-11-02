def solution():
    # On Sunday
    sunday_pints = 4

    # On Monday
    monday_pints = sunday_pints * 3

    # On Tuesday
    tuesday_pints = monday_pints / 3

    # On Wednesday
    wednesday_pints = monday_pints / 2 - tuesday_pints

    total_pints = sunday_pints + monday_pints + tuesday_pints + wednesday_pints
    result = total_pints
    return result

print(solution())