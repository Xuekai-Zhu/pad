def solution():
    waffle_time = 10  # Time taken to cook a batch of waffles in minutes
    steak_time = 6  # Time taken to cook a chicken-fried steak in minutes
    num_steaks = 3  # Number of chicken-fried steaks to be cooked

    # Calculate the total time to cook the waffles and steaks
    total_time = (waffle_time + (steak_time * num_steaks))

    result = total_time
    return result

print(solution())