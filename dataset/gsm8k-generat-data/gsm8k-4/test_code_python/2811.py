def solution():
    """Brenda raises mice, and her adult mice recently had three litters of 8 each. She gave a sixth of the baby mice to her friend Robbie to keep as pets. She sold three times the number of babies she gave Robbie to a pet store. Half of the remaining mice were sold to snake owners as feeder mice. How many baby mice did Brenda have left?"""
    # Define the initial number of baby mice
    baby_mice = 3 * 8

    # Calculate the number of baby mice given to Robbie
    robbie_mice = baby_mice // 6

    # Calculate the number of baby mice sold to the pet store
    pet_store_mice = 3 * robbie_mice

    # Calculate the number of remaining mice
    remaining_mice = baby_mice - robbie_mice - pet_store_mice

    # Calculate the number of mice sold to snake owners as feeder mice
    feeder_mice = remaining_mice // 2

    # Calculate the number of baby mice left
    baby_mice_left = remaining_mice - feeder_mice

    result = baby_mice_left
    return result

print(solution())