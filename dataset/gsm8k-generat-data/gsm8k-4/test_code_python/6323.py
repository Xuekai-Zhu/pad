def solution():
    """There were 90 jellybeans in a jar. Samantha snuck 24 jellybeans out of the jar, without being seen. Shelby ate 12 jellybeans from the jar. Their mom, Shannon, refilled the jar with half as much as Samantha and Shelby took out. How many jellybeans are in the jar now?"""
    # Define the initial number of jellybeans
    initial_jellybeans = 90

    # Calculate how many jellybeans were taken out
    taken_out = 24 + 12

    # Calculate how many jellybeans Shannon refilled
    refilled = taken_out / 2

    # Calculate the current number of jellybeans in the jar
    current_jellybeans = initial_jellybeans - taken_out + refilled

    result = current_jellybeans
    return result

print(solution())