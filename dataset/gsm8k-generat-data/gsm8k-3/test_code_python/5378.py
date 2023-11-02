def solution():
    """James builds a 20 story building.  The first 10 stories are each 12 feet tall each.  The remaining floors are each 3 feet taller.  How tall is the building?"""
    # Define the number of stories in the building
    NUM_STORIES = 20

    # Define the height of the first 10 stories
    FIRST_10_HEIGHT = 12

    # Define the additional height of the remaining stories
    ADDITIONAL_HEIGHT = 3

    # Calculate the total height of the first 10 stories
    first_10_total_height = 10 * FIRST_10_HEIGHT

    # Calculate the total height of the remaining stories
    remaining_total_height = (NUM_STORIES - 10) * (FIRST_10_HEIGHT + ADDITIONAL_HEIGHT)

    # Calculate the total height of the building
    total_height = first_10_total_height + remaining_total_height

    # Display the total height
    result = total_height
    return result

print(solution())