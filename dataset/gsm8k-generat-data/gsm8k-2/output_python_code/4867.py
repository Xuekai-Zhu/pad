def solution():
    """Ishmael was monitoring whales out at sea for conservation purposes. Each time he takes a trip to sea, he sees a different group of whales. On his first trip, he counts 28 male whales and twice as many female whales. On his second trip, he sees 8 baby whales, each travelling with their parents. On his third trip, he counts half as many male whales as the first trip and the same number of female whales as on the first trip. In total, how many whales were out at sea during Ishmael’s monitoring?"""
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