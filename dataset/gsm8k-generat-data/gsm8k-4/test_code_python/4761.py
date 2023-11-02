def solution():
    """There are 100 jellybeans in a glass jar. Mrs. Copper’s kindergarten class normally has 24 kids, but 2 children called in sick and stayed home that day. The remaining children who attended school eat 3 jellybeans each. How many jellybeans are still left in the jar?"""
    # Define the initial number of jellybeans
    initial_jellybeans = 100

    # Define the number of kids who attended school
    attended_school = 24 - 2

    # Calculate the number of jellybeans eaten by the kids
    jellybeans_eaten = attended_school * 3

    # Calculate the number of jellybeans left in the jar
    jellybeans_left = initial_jellybeans - jellybeans_eaten

    # return the result
    result = jellybeans_left
    return result

print(solution())