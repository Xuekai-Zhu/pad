def solution():
    """Hannah ran 9 kilometers on Monday. She ran 4816 meters on Wednesday and 2095 meters on Friday. 
    How many meters farther did she run on Monday than Wednesday and Friday combined?"""
    monday_distance = 9000
    wednesday_distance = 4816
    friday_distance = 2095
    combined_distance = wednesday_distance + friday_distance
    difference = monday_distance - combined_distance
    result = difference
    return result

print(solution())