def solution():
    
    total_cards = 500
    ellis_ratio = 11
    orion_ratio = 9
    total_ratio = ellis_ratio + orion_ratio
    ellis_share = (ellis_ratio / total_ratio) * total_cards
    orion_share = (orion_ratio / total_ratio) * total_cards
    difference = ellis_share - orion_share
    result = difference
    return result

print(solution())