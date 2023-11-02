def solution():
    """Ryan's party was 4 times as huge as Taylor's birthday party. If both parties combined had 240 people, how many people were there at Ryan's party?"""
    # Let's assume the number of people at Taylor's party is x
    # Ryan's party is 4 times as huge as Taylor's party, so the number of people at Ryan's party is 4x

    # The total number of people is 240, so:
    # x + 4x = 240
    # 5x = 240
    # x = 48

    # Now that we know x, we can find the number of people at Ryan's party:
    ryan_party = 4 * 48

    # Return the result
    result = ryan_party
    return result

print(solution())