def solution():
    
    # Define the length of the shark and the length of the remoras
    shark_length = 10
    remoras_length = 2

    # Calculate the combined length of the remoras
    remoras_total_length = remoras_length * 2

    # Calculate the percentage of the shark's body length
    shark_percentage = (shark_length / remoras_total_length) * 100

    # Display the percentage of the shark's body length
    result = shark_percentage
    return result

print(solution())