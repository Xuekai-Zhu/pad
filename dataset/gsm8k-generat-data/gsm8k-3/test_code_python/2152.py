def solution():
    """Aunt Angela has 70 jellybeans in a jar.  She wants to divide them equally and give them to her 3 nephews and 2 nieces.  How many jellybeans did each nephew or niece receive?"""
    # Define the number of nephews and nieces
    NUM_NEPHEWS = 3
    NUM_NIECES = 2

    # Define the total number of jellybeans
    TOTAL_JELLYBEANS = 70

    # Calculate the number of jellybeans each nephew or niece received
    jellybeans_per_person = TOTAL_JELLYBEANS // (NUM_NEPHEWS + NUM_NIECES)

    # Display the number of jellybeans each nephew or niece received
    result = jellybeans_per_person
    return result

print(solution())