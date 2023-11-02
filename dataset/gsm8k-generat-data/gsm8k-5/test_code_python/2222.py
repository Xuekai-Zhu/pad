def solution():
    total_distance = 36  # Together, Selena and Josh ran 36 miles
    josh_distance = total_distance / 2  # Josh ran half of the total distance
    selena_distance = total_distance - josh_distance  # Selena ran the remaining distance

    result = selena_distance
    return result

print(solution())