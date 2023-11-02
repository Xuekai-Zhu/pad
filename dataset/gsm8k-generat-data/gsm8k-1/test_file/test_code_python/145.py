def solution():
    """Charlie has three times as many Facebook friends as Dorothy. James has four times as many friends on Facebook as Dorothy. If Charlie has 12 friends on Facebook, how many Facebook friends does James have?"""
    charlie_friends = 12
    dorothy_friends = charlie_friends / 3
    james_friends = dorothy_friends * 4
    result = james_friends
    return result

print(solution())