def solution():
    
    total_distance = 70
    first_dog_distance = 2 * 7
    second_dog_distance = total_distance - first_dog_distance
    days = 7
    second_dog_average = second_dog_distance / days
    result = second_dog_average
    return result

print(solution())