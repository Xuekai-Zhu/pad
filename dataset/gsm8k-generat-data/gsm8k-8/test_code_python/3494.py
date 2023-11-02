def solution():
    # Define the size of the bathroom and kitchen floors
    bathroom_size = 24
    kitchen_size = 80

    # Calculate the total size of the floors
    total_size = bathroom_size + kitchen_size

    # Calculate the time it takes to mop the floors
    mopping_time = total_size / 8
    result = mopping_time
    return result

print(solution())