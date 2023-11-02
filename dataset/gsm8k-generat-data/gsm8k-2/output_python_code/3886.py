def solution():
    """Bingo has two dogs. On average, they walk a total of 70 miles a week. The first dog walks an average of 2 miles a day. How many miles a day does the other dog average?"""
    total_miles_per_week = 70
    first_dog_miles_per_day = 2
    first_dog_total_miles_per_week = first_dog_miles_per_day * 7
    second_dog_total_miles_per_week = total_miles_per_week - first_dog_total_miles_per_week
    second_dog_miles_per_day = second_dog_total_miles_per_week / 7
    result = second_dog_miles_per_day
    return result

print(solution())