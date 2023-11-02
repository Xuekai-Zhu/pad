def solution():
    """A party venue has 4 tables that seat 6 people each, 16 tables that seat 4 people each, and 8 round tables that seat 10 people each. What is the total capacity of all the tables at the party venue?"""
    table_6_people = 4
    table_4_people = 16
    round_table_10_people = 8
    capacity_6_people = table_6_people * 6
    capacity_4_people = table_4_people * 4
    capacity_10_people = round_table_10_people * 10
    total_capacity = capacity_6_people + capacity_4_people + capacity_10_people
    result = total_capacity
    return result

print(solution())