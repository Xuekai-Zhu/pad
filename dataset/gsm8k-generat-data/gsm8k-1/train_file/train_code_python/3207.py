def solution():
    """Sarah buys 20 pencils on Monday. Then she buys 18 more pencils on Tuesday. On Wednesday she buys triple the number of pencils she did on Tuesday. How many pencils does she have?"""
    monday_pencils = 20
    tuesday_pencils = 18
    wednesday_pencils = tuesday_pencils * 3
    total_pencils = monday_pencils + tuesday_pencils + wednesday_pencils
    result = total_pencils
    return result

print(solution())