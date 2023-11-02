def solution():
    stories = 6  # Tom needs to lower a rope down 6 stories
    story_length = 10  # One story is 10 feet in length
    rope_length = 20  # The rope being sold is 20 feet in length
    loss_percentage = 25  # 25% of the length is lost when lashing them together

    # Calculate the total length of rope needed
    total_length = stories * story_length
    length_with_loss = total_length / (1 - loss_percentage/100)
    
    # Calculate the number of pieces of rope needed
    pieces_of_rope = length_with_loss // rope_length + 1
    result = pieces_of_rope
    return result

print(solution())