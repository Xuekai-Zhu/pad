def solution():
    """Jack and Rose want to start a dog-walking business after school. They made 1,236 flyers to hand out around their neighborhood. Jack handed 120 flyers while Rose handed 320 flyers. How many flyers are left to be handed out around?"""
    total_flyers = 1236
    flyers_handed_out = 120 + 320
    flyers_left = total_flyers - flyers_handed_out
    result = flyers_left
    return result

print(solution())