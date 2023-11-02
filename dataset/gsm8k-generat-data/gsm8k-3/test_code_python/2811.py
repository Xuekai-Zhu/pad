def solution():
    """Brenda raises mice, and her adult mice recently had three litters of 8 each. She gave a sixth of the baby mice to her friend Robbie to keep as pets. She sold three times the number of babies she gave Robbie to a pet store. Half of the remaining mice were sold to snake owners as feeder mice. How many baby mice did Brenda have left?"""
    # Define the number of litters of mice and the number of mice per litter
    NUM_LITTERS = 3
    NUM_MICE_PER_LITTER = 8

    # Calculate the total number of baby mice
    total_babies = NUM_LITTERS * NUM_MICE_PER_LITTER

    # Calculate the number of mice given to Robbie
    robbie_mice = total_babies // 6

    # Calculate the number of mice sold to the pet store
    pet_store_mice = 3 * robbie_mice

    # Calculate the number of mice remaining
    remaining_mice = total_babies - robbie_mice - pet_store_mice

    # Calculate the number of mice sold as feeder mice
    feeder_mice = remaining_mice // 2

    # Calculate the number of mice left
    left_mice = remaining_mice - feeder_mice

    # Display the number of baby mice left
    result = left_mice
    return result

print(solution())