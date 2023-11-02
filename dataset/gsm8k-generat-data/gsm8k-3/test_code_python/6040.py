def solution():
    """Jack and Rose want to start a dog-walking business after school. They made 1,236 flyers to hand out around their neighborhood. Jack handed 120 flyers while Rose handed 320 flyers. How many flyers are left to be handed out around?"""
    # Define the number of flyers Jack and Rose handed out
    jack_flyers = 120
    rose_flyers = 320

    # Calculate the total number of flyers handed out
    total_flyers = jack_flyers + rose_flyers

    # Calculate the number of flyers left to be handed out around the neighborhood
    remaining_flyers = 1236 - total_flyers

    # Display the number of flyers left to be handed out
    result = remaining_flyers
    return result

print(solution())