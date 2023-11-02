def solution():
    """In his company, Kenzo has 80 office chairs with five legs each and 20 round tables with three legs each. If after a month 40% of the chairs are damaged and have to be disposed of, calculate the total number of legs of furniture Kenzo has remaining in his company."""

    # calculate the number of legs of the chairs before any damage
    chairs = 80
    legs_per_chair = 5
    total_legs_chairs = chairs * legs_per_chair

    # calculate the number of legs of the tables
    tables = 20
    legs_per_table = 3
    total_legs_tables = tables * legs_per_table

    # calculate the number of damaged chairs and subtract from the total number of chairs
    damaged_chairs = 0.4 * chairs
    remaining_chairs = chairs - damaged_chairs

    # calculate the total number of legs after damage
    total_legs = (remaining_chairs * legs_per_chair) + total_legs_tables

    result = total_legs
    return result

print(solution())