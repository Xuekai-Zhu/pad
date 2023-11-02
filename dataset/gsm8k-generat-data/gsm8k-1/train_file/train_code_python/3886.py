def solution():
    """Bingo has two dogs. On average, they walk a total of 70 miles a week. The first dog walks an average of 2 miles a day. How many miles a day does the other dog average?"""
    total_distance = 70
    first_dog_distance = 2 * 7
    second_dog_distance = total_distance - first_dog_distance
    days = 7
    second_dog_average = second_dog_distance / days
    result = second_dog_average
    return result

print(solution())