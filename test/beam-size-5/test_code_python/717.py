def solution():
    
    # Define the tap rates and the time raised
    right_rate = 300
    left_rate = 250
    missed_rate = 200
    missed_time = 5 - 2

    # Calculate the total tap rate
    total_right_rate = right_rate * missed_time
    total_left_rate = left_rate * missed_time
    total_rate = total_right_rate + total_left_rate + total_rate

    # Calculate the combined total taps
    combined_total = total_right_rate + total_left_rate

    # Display the combined total taps
    result = combined_total
    return result

print(solution())