def solution():
    """Ben's potato gun can launch a potato 6 football fields. If a football field is 200 yards long and Ben's dog can run 400 feet/minute, how many minutes will it take his dog to fetch a potato he launches?"""
    football_field_length = 200 * 3 # convert yards to feet
    total_distance = football_field_length * 6
    dog_speed = 400 # feet per minute
    time_taken = total_distance / dog_speed
    result = time_taken
    
    return result

print(solution())