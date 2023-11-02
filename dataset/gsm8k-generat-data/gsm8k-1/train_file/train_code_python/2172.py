def solution():
    """At the Taylor family reunion, there were 45 kids and 123 adults. When they sat down to eat, there were 14 tables. How many people sat at each table?"""
    total_people = 45 + 123
    num_tables = 14
    people_per_table = total_people // num_tables
    result = people_per_table
    return result

print(solution())