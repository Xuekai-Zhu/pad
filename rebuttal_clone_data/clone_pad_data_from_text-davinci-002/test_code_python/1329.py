def solution():
    total_votes = 1150
    johns_votes = 150
    remaining_votes = total_votes - johns_votes
    james_votes = remaining_votes * 0.7
    third_guys_votes = remaining_votes - james_votes
    difference = third_guys_votes - johns_votes
    result = difference
    return result

print(solution())