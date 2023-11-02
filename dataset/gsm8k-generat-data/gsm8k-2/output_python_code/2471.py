def solution():
    """Karen packs peanut butter sandwiches in her daughter's lunch 2 randomly chosen days of the week. The other 3 school days, she packs a ham sandwich. She packs a piece of cake on one randomly chosen day and cookies the other four days. What is the probability, expressed as a percentage, that Karen packs a ham sandwich and cake on the same day?"""
    ham_probability = 3 / 5
    cake_probability = 1 / 5
    probability = ham_probability * cake_probability * 100
    result = probability
    return result

print(solution())