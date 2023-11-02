def solution():
    """Sarah buys 20 pencils on Monday. Then she buys 18 more pencils on Tuesday. On Wednesday she buys triple the number of pencils she did on Tuesday. How many pencils does she have?"""
    # Define the number of pencils bought on each day
    monday_pencils = 20
    tuesday_pencils = 18
    wednesday_pencils = tuesday_pencils * 3

    # Calculate the total number of pencils Sarah has
    total_pencils = monday_pencils + tuesday_pencils + wednesday_pencils

    # return the result
    result = total_pencils
    return result

print(solution())