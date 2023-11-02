def solution():
    """After a visit to the newly opened aquarium, 40 percent of the aquarium visitors fell ill from a mysterious disease. If there were 500 visitors, how many of them did not fall ill?"""
    # Define the percentage of visitors who fell ill
    ILL_PERCENTAGE = 40

    # Get the number of visitors
    total_visitors = 500

    # Calculate the number of visitors who did not fall ill
    visitors_not_ill = total_visitors * (100 - ILL_PERCENTAGE) / 100

    # Display the number of visitors who did not fall ill
    result = visitors_not_ill
    return result

print(solution())