def solution():
    """Jack, who weighs 60 pounds, wants to play on the see-saw with his cousin Anna, who weighs 40 pounds. How many 4-pound rocks does Jack need to hold to make their weights equal?"""
    jack_weight = 60
    anna_weight = 40
    weight_difference = jack_weight - anna_weight
    rocks_needed = weight_difference / 4
    result = rocks_needed
    return result

print(solution())