def solution():
    """Ryan's party was 4 times as huge as Taylor's birthday party. If both parties combined had 240 people, how many people were there at Ryan's party?"""
    total_people = 240
    ratio = 4
    ryan_ratio = ratio / (1 + ratio)
    ryan_people = ryan_ratio * total_people
    result = ryan_people
    return result

print(solution())