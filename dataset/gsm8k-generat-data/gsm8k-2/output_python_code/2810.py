def solution():
    """Brenda raises mice, and her adult mice recently had three litters of 8 each. She gave a sixth of the baby mice to her friend Robbie to keep as pets. She sold three times the number of babies she gave Robbie to a pet store. Half of the remaining mice were sold to snake owners as feeder mice. How many baby mice did Brenda have left?"""
    total_baby_mice = 3 * 8
    robbie_mice = total_baby_mice // 6
    pet_store_mice = 3 * robbie_mice
    remaining_mice = total_baby_mice - robbie_mice - pet_store_mice
    feeder_mice = remaining_mice // 2
    brenda_left_with = remaining_mice - feeder_mice
    result = brenda_left_with
    return result

print(solution())