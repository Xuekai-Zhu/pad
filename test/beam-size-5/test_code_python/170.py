def solution():
    
    # Define the number of potatoes and the time it takes to peel one potato
    potatoes = 60
    time_per_potato = 60 / 2

    # Calculate the time it takes to peel one potato
    time_peel_potato = time_per_potato / 2

    # Calculate the time it takes to cut up the potatoes
    time_cut_potato = time_per_potato * 5

    # Calculate the total time it takes to prep the potatoes
    total_time = time_peel_potato + time_cut_potato

    # return the result
    result = total_time
    return result

print(solution())