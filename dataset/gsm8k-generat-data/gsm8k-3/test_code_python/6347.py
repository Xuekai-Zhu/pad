def solution():
    """Karen is a dog groomer. Rottweilers take 20 minutes to groom, border collies take 10 minutes to groom, and chihuahuas take 45 minutes to groom because they ferociously resist. How many minutes will it take Karen to groom 6 Rottweilers, 9 border collies and 1 chihuahua?"""
    # Define the grooming time for each type of dog
    ROTTWEILER_TIME = 20
    BORDER_COLLIE_TIME = 10
    CHIHUAHUA_TIME = 45

    # Define the number of each type of dog to be groomed
    num_rottweilers = 6
    num_border_collies = 9
    num_chihuahuas = 1

    # Calculate the total grooming time
    total_time = (num_rottweilers * ROTTWEILER_TIME) + (num_border_collies * BORDER_COLLIE_TIME) + (num_chihuahuas * CHIHUAHUA_TIME)

    # Display the total grooming time
    result = total_time
    return result

print(solution())