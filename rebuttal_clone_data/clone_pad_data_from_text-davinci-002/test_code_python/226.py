def solution():
    """There are 32 tables in a hall. Half the tables have 2 chairs each, 5 have 3 chairs each and the rest have 4 chairs each. How many chairs in total are in the hall?"""
    tables_total = 32
    tables_with_two_chairs = tables_total / 2
    tables_with_three_chairs = 5
    tables_with_four_chairs = tables_total - tables_with_two_chairs - tables_with_three_chairs
    chairs_with_two = tables_with_two_chairs * 2
    chairs_with_three = tables_with_three_chairs * 3
    chairs_with_four = tables_with_four_chairs * 4
    total_chairs = chairs_with_two + chairs_with_three + chairs_with_four
    result = total_chairs
    return result

print(solution())