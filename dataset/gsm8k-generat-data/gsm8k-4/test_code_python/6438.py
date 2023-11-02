def solution():
    """A woodworker is crafting enough furniture legs for their projects. They have made a total of 40 furniture legs so far,
     and this is the exact amount they needed for everything they’re building. If the woodworker is using these legs for 
     their tables and chairs and they have built 6 chairs, how many tables have they made?"""
    # Define the number of legs for a chair and a table
    chair_legs = 4
    table_legs = 4

    # Calculate the number of legs used for the chairs
    chair_legs_used = chair_legs * 6

    # Calculate the remaining legs for the tables
    table_legs_remaining = 40 - chair_legs_used

    # Calculate the number of tables made
    tables_made = table_legs_remaining / table_legs

    # return the result
    result = tables_made
    return result

print(solution())