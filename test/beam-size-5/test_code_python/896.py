def solution():
    
    # Define the number of pages Daniel read yesterday and today
    daniel_yesterday = 10
    daniel_today = 13

    # Calculate the number of pages Denise read yesterday and today
    denise_yesterday = daniel_yesterday + 5
    denise_today = daniel_today * 2

    # Calculate the difference in the number of pages Denise and Daniel read
    difference = denise_yesterday - denise_today

    # Display the difference in the number of pages Denise read
    result = difference
    return result

print(solution())