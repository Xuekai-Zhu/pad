def solution():
    """There are 100 jellybeans in a glass jar.  Mrs. Copper’s kindergarten class normally has 24 kids, but 2 children called in sick and stayed home that day. The remaining children who attended school eat 3 jellybeans each. How many jellybeans are still left in the jar?"""
    # Define the initial number of jellybeans in the jar
    INITIAL_JELLYBEANS = 100

    # Define the number of kids who attended school
    kids_attended = 24 - 2

    # Calculate the total number of jellybeans eaten
    jellybeans_eaten = kids_attended * 3

    # Calculate the remaining number of jellybeans in the jar
    jellybeans_remaining = INITIAL_JELLYBEANS - jellybeans_eaten

    # Display the remaining number of jellybeans
    result = jellybeans_remaining
    return result

print(solution())