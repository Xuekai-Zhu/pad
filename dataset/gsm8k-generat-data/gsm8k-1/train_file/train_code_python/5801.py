def solution():
    """Hannah ran 9 kilometers on Monday. She ran 4816 meters on Wednesday and 2095 meters on Friday. How many meters farther did she run on Monday than Wednesday and Friday combined?"""
    monday_meters = 9000
    wednesday_meters = 4816
    friday_meters = 2095
    total_meters = wednesday_meters + friday_meters
    difference = monday_meters - total_meters
    result = difference
    return result

print(solution())