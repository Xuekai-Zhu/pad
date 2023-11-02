def solution():
    num_stories = 6
    story_height = 10  # feet
    rope_length = 20  # feet
    loss_percentage = 0.25  # 25% loss when lashing ropes together

    # Calculate the total height that Tom needs to lower the rope
    total_height = num_stories * story_height

    # Calculate the length of rope Tom needs after factoring in the loss from lashing
    usable_rope_length = rope_length * (1 - loss_percentage)

    # Calculate the number of pieces of rope Tom needs to buy
    num_rope_pieces = total_height / usable_rope_length
    result = num_rope_pieces
    return result

print(solution())