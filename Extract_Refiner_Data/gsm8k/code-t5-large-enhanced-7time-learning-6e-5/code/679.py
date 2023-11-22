def solution():
    
    # Define the time it takes to mow the lawn in "turtle" mode and "rabbit" mode in minutes
    turtle_time = 1
    rabbit_time = 40

    # Calculate the time it takes to mow the lawn in half turtle mode and half rabbit mode
    half_turtle_time = turtle_time / 2
    half_rabbit_time = rabbit_time / 2

    # Calculate the total time it takes to mow the lawn
    total_time = half_turtle_time + half_rabbit_time

    # Display the total time
    result = total_time
    return result

print(solution())