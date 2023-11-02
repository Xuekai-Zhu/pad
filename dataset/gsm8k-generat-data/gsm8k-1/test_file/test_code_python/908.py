def solution():
    """John drinks a bottle of water every half hour. A normal sudoku puzzle takes him 45 minutes. An extreme sudoku takes 4 times that long. How many bottles of water does he drink in that time?"""
    water_per_hour = 2 # John drinks two bottles of water per hour
    normal_sudoku_time = 45 # minutes
    extreme_sudoku_time = 4 * normal_sudoku_time # minutes
    total_time = normal_sudoku_time + extreme_sudoku_time # minutes
    total_water_consumed = (total_time / 30) * water_per_hour # calculate bottles of water consumed
    result = total_water_consumed
    return result

print(solution())