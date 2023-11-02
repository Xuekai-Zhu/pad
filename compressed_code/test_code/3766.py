def solution():
    
    first_trip_male = 28
    first_trip_female = 2 * first_trip_male
    second_trip_babies = 8
    second_trip_parents = second_trip_babies * 2
    third_trip_male = first_trip_male / 2
    third_trip_female = first_trip_female
    total_whales = first_trip_male + first_trip_female + second_trip_babies + second_trip_parents + third_trip_male + third_trip_female
    result = total_whales
    return result

print(solution())