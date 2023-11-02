def solution():
    """Together Felipe and Emilio needed a combined time of 7.5 years to build their homes. Felipe finished in half the time of Emilio. How many months did it take Felipe to build his house?"""
    # Define the total time taken by Felipe and Emilio
    total_time = 7.5 # years

    # Let's assume that Emilio took 'x' years to build his house
    emilio_time = x

    # Felipe took half the time of Emilio, so
    felipe_time = x / 2

    # Calculate the total time taken by both of them together
    total_time_calculated = emilio_time + felipe_time

    # We know that total_time_calculated = total_time
    # So, we can solve for 'x'
    x = 2 * (total_time - felipe_time)

    # Convert the time taken by Felipe into months
    felipe_time_months = felipe_time * 12

    # Display the time taken by Felipe in months
    result = felipe_time_months
    return result

print(solution())