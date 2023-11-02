def solution():
    time_per_rottweiler = 20  # Rottweilers take 20 minutes to groom
    time_per_border_collie = 10  # Border collies take 10 minutes to groom
    time_per_chihuahua = 45  # Chihuahuas take 45 minutes to groom
    num_rottweilers = 6  # Karen has to groom 6 Rottweilers
    num_border_collies = 9  # Karen has to groom 9 Border Collies
    num_chihuahuas = 1  # Karen has to groom 1 Chihuahua

    # Calculate the total time Karen will spend grooming all the dogs
    total_time = (time_per_rottweiler * num_rottweilers) + (time_per_border_collie * num_border_collies) + (time_per_chihuahua * num_chihuahuas)

    result = total_time
    return result

print(solution())