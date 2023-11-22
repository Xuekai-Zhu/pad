def solution():
    
    # Define the number of gifts to wrap each person
    family_gifts = 6
    friend_gifts = 4
    teacher_gifts = 2

    # Define the total number of gifts
    total_gifts = family_gifts + friend_gifts + teacher_gifts

    # Define the total length of ribbon
    total_ribbon = 144

    # Calculate the length of ribbon used for each gift bow
    bow_length = total_ribbon / total_gifts

    # Display the length of ribbon used for each gift bow
    result = bow_length
    return result

print(solution())