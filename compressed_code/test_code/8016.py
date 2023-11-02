def solution():
    
    total_babies = 3 * 8
    robby_babies = total_babies / 6
    petstore_babies = 3 * robby_babies
    remaining_babies = total_babies - robby_babies - petstore_babies
    feeder_babies = remaining_babies / 2
    babies_left = remaining_babies - feeder_babies
    result = babies_left
    return result

print(solution())