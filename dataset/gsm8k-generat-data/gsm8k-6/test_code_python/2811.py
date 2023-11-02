def solution():
    # Calculate the total number of baby mice Brenda had
    total_babies = 3 * 8  # three litters of 8 each
    # Calculate the number of babies given to Robbie
    robbie_babies = total_babies // 6  # a sixth of the babies
    # Calculate the number of babies sold to the pet store
    pet_store_babies = 3 * robbie_babies  # three times the number given to Robbie
    # Calculate the remaining number of babies
    remaining_babies = total_babies - robbie_babies - pet_store_babies
    # Calculate the number of babies sold as feeder mice
    feeder_babies = remaining_babies // 2  # half of the remaining babies
    # Calculate the number of babies left
    babies_left = remaining_babies - feeder_babies

    result = babies_left
    return result

print(solution())