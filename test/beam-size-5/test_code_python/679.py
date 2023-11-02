def solution():
    
    # Define the time it takes to mow the lawn in "turtle" mode
    turtle_time = 1

    # Define the time it takes to mow the lawn in "rabbit" mode
    rabbit_time = 40

    # Calculate the time it takes to mow the lawn in "turtle" mode
    turtle_time = turtle_time / 2

    # Calculate the time it takes to mow the lawn in "rabbit" mode
    rabbit_time = rabbit_time / 2

    # Calculate the total time it takes to mow the lawn
    total_time = turtle_time + rabbit_time

    # return the result
    result = total_time
    return result

print(solution())