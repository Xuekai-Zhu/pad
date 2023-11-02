def solution():
    """Hannah ran 9 kilometers on Monday. She ran 4816 meters on Wednesday and 2095 meters on Friday. How many meters farther did she run on Monday than Wednesday and Friday combined?"""
    # Define the distances run on each day
    monday_distance = 9000
    wednesday_distance = 4816
    friday_distance = 2095

    # Calculate the total distance run on Wednesday and Friday
    wednesday_friday_distance = wednesday_distance + friday_distance

    # Calculate the difference between the distance run on Monday and Wednesday/Friday combined
    difference = monday_distance - wednesday_friday_distance

    # return the result
    result = difference
    return result

print(solution())