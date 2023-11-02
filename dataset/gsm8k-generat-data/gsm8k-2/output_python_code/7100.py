def solution():
    """On Sunday Alice bought 4 pints of strawberry ice cream. The next day she went back and bought three times that number of pints. On Tuesday she bought one-third of the number of pints she bought the day before. On Wednesday she returned half of the pints she bought the day before because they were expired. How many pints of ice cream did she have on Wednesday?"""
    sunday_pints = 4
    monday_pints = 3 * sunday_pints
    tuesday_pints = monday_pints // 3
    wednesday_pints = monday_pints // 2
    total_pints = sunday_pints + monday_pints + tuesday_pints - wednesday_pints
    result = total_pints
    return result

print(solution())