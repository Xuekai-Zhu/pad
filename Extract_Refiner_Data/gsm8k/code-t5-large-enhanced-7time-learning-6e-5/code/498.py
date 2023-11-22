def solution():
    
    # Define the number of friends and the number of gifts they want for their friends
    NUM_FRIENDS = 5
    FRIENDS_5 = 5
    FRIENDS_2 = 2
    FRIENDS_3 = 3
    FRIENDS_4 = 10

    # Calculate the total number of gifts needed
    total_gifts = NUM_FRIENDS * FRIENDS_5 + NUM_FRIENDS * FRIENDS_2 + NUM_FRIENDS * FRIENDS_3 + FRIENDS_4 + FRIENDS_5 + FRIENDS_2 + FRIENDS_3 + FRIENDS_4

    # Display the total number of gifts
    result = total_gifts
    return result

print(solution())