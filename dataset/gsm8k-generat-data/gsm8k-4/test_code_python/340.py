def solution():
    """Tom needs to lower a rope down 6 stories. One story is 10 feet. The only rope being sold is 20 feet long but you lose 25% when lashing them together. How many pieces of rope will he need to buy?"""
    # Define the height of one story and the total height to be covered
    story_height = 10
    total_height = 6 * story_height

    # Define the length of one rope and the percentage lost when lashing them together
    rope_length = 20
    loss_percentage = 0.25

    # Calculate the effective length of one rope after lashing
    effective_rope_length = rope_length * (1 - loss_percentage)

    # Calculate the number of ropes needed to cover the total height, rounding up to the nearest whole number
    ropes_needed = math.ceil(total_height / effective_rope_length)

    # return the result
    result = ropes_needed
    return result

print(solution())