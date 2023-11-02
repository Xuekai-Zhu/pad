def solution():
    """Two thirds of Jana's puppies are Pomeranians. One third of the Pomeranians are girls. If there are 6 Pomeranian girls, how many puppies does Jana have?"""
    pomeranian_girls = 6
    pomeranians = pomeranian_girls * 3
    total_puppies = pomeranians * (2/3)
    result = total_puppies
    return result

print(solution())