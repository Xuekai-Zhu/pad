def solution():
    
    # Define the number of potatoes and the number of hash browns per potato
    num_potatoes = 96
    num_browns_per_potato = 36 / 6

    # Calculate the total number of browns that can be made
    total_browns = num_browns_per_potato * num_potatoes

    # Display the total number of browns
    result = total_browns
    return result

print(solution())