def solution():
    """Alan counted how many chairs the office canteen has. It has 2 round tables and 2 rectangular tables. Each round table has 6 chairs, and each rectangular table has 7 chairs. How many chairs are there in all?"""
    round_chairs = 2 * 6
    rectangular_chairs = 2 * 7
    total_chairs = round_chairs + rectangular_chairs
    result = total_chairs
    return result

print(solution())