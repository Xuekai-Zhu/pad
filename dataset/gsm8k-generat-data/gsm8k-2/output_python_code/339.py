def solution():
    """Tom needs to lower a rope down 6 stories. One story is 10 feet. The only rope being sold is 20 feet long but you lose 25% when lashing them together. How many pieces of rope will he need to buy?"""
    story_height = 10
    total_height = 6 * story_height
    rope_length = 20
    loss_percentage = 25
    actual_rope_length = rope_length - (rope_length * loss_percentage / 100)
    pieces_of_rope_needed = total_height / actual_rope_length
    result = round(pieces_of_rope_needed)
    return result

print(solution())