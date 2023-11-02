def solution():
    """A pole is 20 meters long. It got cut in a way that left it 30% shorter. How long is the pole?"""
    initial_length = 20
    percent_shorter = 30
    new_length = initial_length * (100 - percent_shorter) / 100
    result = new_length
    return result

print(solution())