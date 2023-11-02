def solution():
    """Brenda raises mice, and her adult mice recently had three litters of 8 each. She gave a sixth of the baby mice to her friend Robbie to keep as pets. She sold three times the number of babies she gave Robbie to a pet store. Half of the remaining mice were sold to snake owners as feeder mice. How many baby mice did Brenda have left?"""
    total_babies = 3 * 8
    robby_babies = total_babies / 6
    petstore_babies = 3 * robby_babies
    remaining_babies = total_babies - robby_babies - petstore_babies
    feeder_babies = remaining_babies / 2
    babies_left = remaining_babies - feeder_babies
    result = babies_left
    return result

print(solution())