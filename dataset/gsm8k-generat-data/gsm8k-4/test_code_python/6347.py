def solution():
    """Karen is a dog groomer. Rottweilers take 20 minutes to groom, border collies take 10 minutes to groom, and chihuahuas take 45 minutes to groom because they ferociously resist. How many minutes will it take Karen to groom 6 Rottweilers, 9 border collies and 1 chihuahua?"""
    # Define the grooming time for each type of dog
    rottweiler_time = 20
    border_collie_time = 10
    chihuahua_time = 45

    # Calculate the total grooming time for all the dogs
    total_time = (6 * rottweiler_time) + (9 * border_collie_time) + chihuahua_time

    # Return the result
    result = total_time
    return result

print(solution())