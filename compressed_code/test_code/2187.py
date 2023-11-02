def solution():
    
    total_baby_mice = 3 * 8
    robbie_mice = total_baby_mice // 6
    pet_store_mice = 3 * robbie_mice
    remaining_mice = total_baby_mice - robbie_mice - pet_store_mice
    feeder_mice = remaining_mice // 2
    brenda_left_with = remaining_mice - feeder_mice
    result = brenda_left_with
    return result

print(solution())