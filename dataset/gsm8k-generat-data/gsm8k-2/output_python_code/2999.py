def solution():
    """A pole is 20 meters long. It got cut in a way that left it 30% shorter. How long is the pole?"""
    pole_length = 20
    cut_percentage = 0.3
    remaining_length = pole_length * (1 - cut_percentage)
    result = remaining_length
    return result

print(solution())