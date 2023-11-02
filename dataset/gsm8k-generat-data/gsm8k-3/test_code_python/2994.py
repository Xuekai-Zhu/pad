def solution():
    """Nadine's dog rolls around in the mud. She spends 10 minutes hosing him off outside, then shampoos him three times, which takes 15 minutes per shampoo. How long does she spend cleaning her dog total?"""
    # Define the time for hosing off and shampooing
    hosing_time = 10
    shampoo_time = 15

    # Calculate the total time for shampooing
    total_shampoo_time = shampoo_time * 3

    # Calculate the total cleaning time
    total_cleaning_time = hosing_time + total_shampoo_time

    # Display the total cleaning time
    result = total_cleaning_time
    return result

print(solution())