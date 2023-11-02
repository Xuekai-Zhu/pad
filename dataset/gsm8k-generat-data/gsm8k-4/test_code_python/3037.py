def solution():
    """After a visit to the newly opened aquarium, 40 percent of the aquarium visitors fell ill from a mysterious disease. If there were 500 visitors, how many of them did not fall ill?"""
    # Define the total number of visitors
    total_visitors = 500

    # Calculate the number of visitors who fell ill
    ill_visitors = total_visitors * 0.4

    # Calculate the number of visitors who did not fall ill
    healthy_visitors = total_visitors - ill_visitors

    # return the result
    result = healthy_visitors
    return result

print(solution())