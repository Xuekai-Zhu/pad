def solution():
    alex_pens = 4
    jane_pens = 16
    weeks_in_month = 4

    # Calculate how many pens Alex will have in total after a month
    total_alex_pens = alex_pens * (2 ** weeks_in_month)

    # Calculate how many more pens Alex will have than Jane
    more_pens_than_jane = total_alex_pens - jane_pens
    result = more_pens_than_jane
    return result

print(solution())