def solution():
    """After Bella’s ballet performance, she received 2 dozen roses from her parents, and 2 roses from each of her 10 dancer friends.  How many roses did Bella receive?"""
    # Define the number of roses in a dozen
    ROSES_PER_DOZEN = 12

    # Calculate the number of roses from Bella's parents
    parent_roses = 2 * ROSES_PER_DOZEN

    # Calculate the number of roses from Bella's friends
    friend_roses = 2 * 10

    # Calculate the total number of roses Bella received
    total_roses = parent_roses + friend_roses

    # Display the total number of roses
    result = total_roses
    return result

print(solution())