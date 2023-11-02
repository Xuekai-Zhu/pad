def solution():
    original_length = 30  # The original commercial is 30 seconds long
    reduction_percentage = 0.3  # The boss wants Ursula to shorten the commercial by 30% 

    # Calculate the amount of time the commercial needs to be shortened by
    reduction_time = original_length * reduction_percentage

    # Calculate the new length of the commercial
    new_length = original_length - reduction_time
    result = new_length
    return result

print(solution())