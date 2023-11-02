def solution():
    """When Jane visited Iran, she visited 6 more than twice as many rehabilitation centers as Han. Han visited 2 less than twice as many rehabilitation centers as Jude did. Jude visited half fewer rehabilitation centers as Lisa did. If Lisa visited 6 rehabilitation centers, how many rehabilitation centers did they all visit assuming they are all different?"""
    # Define the number of rehabilitation centers Lisa visited
    lisa_visited = 6

    # Calculate the number of rehabilitation centers Jude visited
    jude_visited = lisa_visited / 2

    # Calculate the number of rehabilitation centers Han visited
    han_visited = 2 * jude_visited - 2

    # Calculate the number of rehabilitation centers Jane visited
    jane_visited = 2 * han_visited + 6

    # Calculate the total number of unique rehabilitation centers visited by all
    total_visited = len(set([lisa_visited, jude_visited, han_visited, jane_visited]))

    # Display the total number of rehabilitation centers visited
    result = total_visited
    return result

print(solution())