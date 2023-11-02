def solution():
    """Antonov bought 60 candies. He gave a pack of candy to his sister. If a pack of candy has 20 pieces, how many packs does Antonov still have?"""
    total_candies = 60
    candies_given = 20
    packs_remaining = (total_candies - candies_given) // 20
    result = packs_remaining
    return result

print(solution())