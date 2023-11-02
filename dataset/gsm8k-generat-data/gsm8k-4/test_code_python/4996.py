def solution():
    """Rebecca drinks half a bottle of soda a day. She bought three 6-packs of sodas the last time she was at the store. How many bottles of soda will she have left after four weeks?"""
    # Define the initial number of soda bottles
    initial_soda_bottles = 3 * 6

    # Calculate the number of soda bottles she drinks in four weeks
    total_soda_bottles_consumed = 0.5 * 7 * 4

    # Calculate the number of soda bottles she will have left after four weeks
    soda_bottles_left = initial_soda_bottles - total_soda_bottles_consumed

    result = soda_bottles_left
    return result

print(solution())