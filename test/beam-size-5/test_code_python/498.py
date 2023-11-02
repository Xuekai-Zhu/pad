def solution():
    
    # Define the number of gifts needed for each friend
    friend1_gifts = 5
    friend2_gifts = 5
    friend3_gifts = 2

    # Calculate the total number of gifts needed for the 5 friends
    total_friend1_gifts = friend1_gifts + friend2_gifts

    # Calculate the total number of gifts needed for the 3 friends
    total_friend3_gifts = friend3_gifts + friend4_gifts

    # Calculate the total number of gifts Cherrie bought
    total_gifts = total_friend1_gifts + total_friend2_gifts + 10

    # Display the total number of gifts
    result = total_gifts
    return result

print(solution())