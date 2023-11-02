def solution():
    """Holden's current master bedroom is 309 sq ft and his master bath is 150 sq ft. If he wants to add a home office/personal gym divided space that is twice as large as his bedroom and bathroom, how much sq ft will this new room have?"""
    # Define the current sizes of the bedroom and bathroom
    bedroom_size = 309
    bathroom_size = 150

    # Calculate the total area of the bedroom and bathroom
    total_area = bedroom_size + bathroom_size

    # Calculate the desired size of the home office/personal gym space
    new_size = 2 * total_area

    # return the result
    result = new_size
    return result

print(solution())