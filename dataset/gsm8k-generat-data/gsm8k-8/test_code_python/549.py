def solution():
    # Calculate the total number of legs of the office chairs
    chairs_legs = 80 * 5

    # Calculate the total number of legs of the round tables
    tables_legs = 20 * 3

    # Calculate the total number of chairs that are damaged
    damaged_chairs = 0.4 * 80

    # Calculate the total number of legs of the remaining chairs
    remaining_chairs_legs = (80 - damaged_chairs) * 5

    # Calculate the total number of legs of the remaining furniture
    total_legs = remaining_chairs_legs + tables_legs
    result = total_legs
    return result

print(solution())