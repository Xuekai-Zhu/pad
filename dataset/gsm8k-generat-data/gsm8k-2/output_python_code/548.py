def solution():
    """In his company, Kenzo has 80 office chairs with five legs each and 20 round tables with three legs each. If after a month 40% of the chairs are damaged and have to be disposed of, calculate the total number of legs of furniture Kenzo has remaining in his company."""
    num_chairs = 80
    num_tables = 20
    num_legs_chairs = 5
    num_legs_tables = 3
    total_legs = (num_chairs * num_legs_chairs) + (num_tables * num_legs_tables)
    damaged_chairs = int(0.4 * num_chairs)
    remaining_chairs = num_chairs - damaged_chairs
    remaining_legs = remaining_chairs * num_legs_chairs + num_tables * num_legs_tables

    result = remaining_legs
    return result

print(solution())