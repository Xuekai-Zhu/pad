def solution():
    """Jack and Rose want to start a dog-walking business after school. They made 1,236 flyers to hand out around their neighborhood. Jack handed 120 flyers while Rose handed 320 flyers. How many flyers are left to be handed out around?"""
    total_flyers = 1236
    jack_flyers = 120
    rose_flyers = 320
    left_flyers = total_flyers - jack_flyers - rose_flyers
    result = left_flyers
    return result

print(solution())