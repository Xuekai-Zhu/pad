def solution():
    """Tom needs to lower a rope down 6 stories. One story is 10 feet. The only rope being sold is 20 feet long but you lose 25% when lashing them together. How many pieces of rope will he need to buy?"""
    stories = 6
    feet_per_story = 10
    total_feet = stories * feet_per_story
    rope_length = 20
    loss_percent = 25
    actual_rope_length = rope_length - (rope_length * (loss_percent / 100))
    pieces_of_rope = total_feet / actual_rope_length
    result = math.ceil(pieces_of_rope)
    
    return result

print(solution())