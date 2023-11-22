def solution():
    
    # Define the initial number of people wrestled
    initial_people = 20

    # Calculate the number of people he beats
    beats = initial_people * 0.8

    # Calculate the number of people he lost to
    lost_people = initial_people - beats

    # return the result
    result = lost_people
    return result

print(solution())