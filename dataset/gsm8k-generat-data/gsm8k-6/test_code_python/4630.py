def solution():
    num_models = 6
    num_bathing_suits = 2
    num_evening_wear = 3

    # Calculate the total number of runway trips required
    total_trips = num_models * (num_bathing_suits + num_evening_wear)

    # Calculate the total time taken for all runway trips in minutes
    time_taken = total_trips * 2

    result = time_taken
    return result

print(solution())