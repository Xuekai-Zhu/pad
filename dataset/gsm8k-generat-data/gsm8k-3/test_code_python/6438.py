def solution():
    """A woodworker is crafting enough furniture legs for their projects. They have made a total of 40 furniture legs so far,
    and this is the exact amount they needed for everything they’re building. If the woodworker is using these legs for their
    tables and chairs and they have built 6 chairs, how many tables have they made?"""

    # Define the number of legs per chair and table
    LEGS_PER_CHAIR = 4
    LEGS_PER_TABLE = 4

    # Determine the number of legs used for chairs
    legs_for_chairs = 6 * LEGS_PER_CHAIR

    # Determine the number of legs remaining for tables
    legs_for_tables = 40 - legs_for_chairs

    # Determine the number of tables
    tables = legs_for_tables // LEGS_PER_TABLE

    # Display the number of tables
    result = tables
    return result

print(solution())