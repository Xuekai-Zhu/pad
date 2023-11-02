def solution():
    """Tom needs to lower a rope down 6 stories. One story is 10 feet. The only rope being sold is 20 feet long but you lose 25% when lashing them together. How many pieces of rope will he need to buy?"""
    # Define the length of one story
    STORY_LENGTH = 10

    # Calculate the total length of rope needed
    total_length = 6 * STORY_LENGTH

    # Calculate the length of rope that is lost when lashing pieces together
    lost_length = 20 * 0.25

    # Calculate the length of rope needed after lashing
    after_lashing_length = 20 - lost_length

    # Calculate the number of pieces of rope needed
    num_pieces = total_length / after_lashing_length

    # Round up to the nearest integer
    num_pieces = math.ceil(num_pieces)

    # Display the number of pieces of rope needed
    result = num_pieces
    return result

print(solution())