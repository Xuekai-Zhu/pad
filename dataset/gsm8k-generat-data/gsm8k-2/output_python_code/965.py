def solution():
    """Ryan's party was 4 times as huge as Taylor's birthday party. If both parties combined had 240 people, how many people were there at Ryan's party?"""
    total_people = 240
    ryan_party_people = 4 * taylor_party_people
    combined_people = ryan_party_people + taylor_party_people
    ryan_people = combined_people / 5
    result = ryan_people
    return result

print(solution())