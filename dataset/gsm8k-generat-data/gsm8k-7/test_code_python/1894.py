def solution():
    num_poodles_monday = 4
    num_chihuahuas_monday = 2

    num_chihuahuas_tuesday = num_chihuahuas_monday

    num_labradors_wednesday = 4

    time_poodle = 2
    time_chihuahua = 1
    time_labrador = 3

    total_time = 32

    # Calculate the total time spent walking poodles and Chihuahuas on Monday
    total_time_monday = (num_poodles_monday * time_poodle) + (num_chihuahuas_monday * time_chihuahua)

    # Calculate how much time is left for walking dogs on Tuesday and Wednesday
    remaining_time = total_time - total_time_monday

    # Calculate the maximum number of poodles Charlotte can walk on Tuesday with the remaining time
    num_poodles_tuesday = remaining_time // time_poodle
    result = num_poodles_tuesday
    return result

print(solution())