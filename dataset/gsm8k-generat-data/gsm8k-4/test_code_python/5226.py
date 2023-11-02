def solution():
    """A party venue has 4 tables that seat 6 people each, 16 tables that seat 4 people each, and 8 round tables that seat 10 people each. What is the total capacity of all the tables at the party venue?"""
    # Define the number of tables and their capacities
    tables = {
        "table1": 6,
        "table2": 6,
        "table3": 6,
        "table4": 6,
        "table5": 4,
        "table6": 4,
        "table7": 4,
        # ...
        # 16 tables total
        # ...
        "table20": 4,
        "round_table1": 10,
        "round_table2": 10,
        "round_table3": 10,
        # ...
        # 8 round tables total
        # ...
        "round_table8": 10
    }

    # Calculate the total capacity of all tables
    total_capacity = sum(tables.values())

    # Return the result
    result = total_capacity
    return result

print(solution())