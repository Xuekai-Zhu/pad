def solution():
    """A party venue has 4 tables that seat 6 people each, 16 tables that seat 4 people each, and 8 round tables that seat 10 people each. What is the total capacity of all the tables at the party venue?"""
    table_6p = 4 * 6
    table_4p = 16 * 4
    round_table_10p = 8 * 10
    total_capacity = table_6p + table_4p + round_table_10p
    result = total_capacity
    return result

print(solution())