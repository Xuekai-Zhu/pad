def solution():
    
    # Define the number of times the alarm rangs each time
    rang_1 = 4
    rang_2 = 3 * rang_1
    rang_3 = 2 * rang_2

    # Calculate the total number of times the alarm rangs
    total_rangs = rang_1 + rang_2 + rang_3

    # Display the total number of rangs
    result = total_rangs
    return result

print(solution())