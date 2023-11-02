def solution():
    """Nadine's dog rolls around in the mud. She spends 10 minutes hosing him off outside, then shampoos him three times, which takes 15 minutes per shampoo. How long does she spend cleaning her dog total?"""
    # Define the time it takes to hose off the dog
    hose_time = 10

    # Define the time it takes to shampoo the dog once
    shampoo_time = 15

    # Calculate the total time spent shampooing the dog
    total_shampoo_time = shampoo_time * 3

    # Add up the total time spent cleaning the dog
    total_time = hose_time + total_shampoo_time

    result = total_time
    return result

print(solution())