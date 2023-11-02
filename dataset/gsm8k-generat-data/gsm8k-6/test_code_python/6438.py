def solution():
    # Calculate the number of legs used for chairs
    legs_for_chairs = 6 * 4  # Each chair has 4 legs

    # Calculate the number of legs left for tables
    legs_for_tables = 40 - legs_for_chairs

    # Calculate the number of tables
    tables = legs_for_tables // 4  # Each table has 4 legs

    result = tables
    return result

print(solution())