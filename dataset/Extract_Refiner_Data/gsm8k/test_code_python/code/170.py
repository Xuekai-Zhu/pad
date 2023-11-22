def solution():
    
    # Define the number of potatoes and the time it takes to peel and cut them up
    num_potatoes = 60
    time_to_peel_potatoes = num_potatoes * (1/2)
    time_to_cut_potatoes = num_potatoes * 5

    # Calculate the total time it takes to finish prepping the potatoes
    total_time = time_to_peel_potatoes + time_to_cut_potatoes

    # Display the total time
    result = total_time
    return result

print(solution())