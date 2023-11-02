def solution():
    """Bob grew corn in his garden this year and ended up with 50 bushels. This is way too much for him to eat, so he gave some of it away to his friends. His friend Terry took 8 bushels, while Jerry only took 3. He gave 12 bushels to his friend Linda, who runs a food pantry. His neighbor Stacy doesn't eat much corn, but she still accepted 21 ears of corn from him. If each bushel contained 14 ears of corn, how many ears of corn does Bob have left?"""
    total_bushels = 50
    terry_bushels = 8
    jerry_bushels = 3
    linda_bushels = 12
    stacy_ears = 21
    remaining_bushels = total_bushels - terry_bushels - jerry_bushels - linda_bushels
    remaining_ears = remaining_bushels * 14 + stacy_ears
    result = remaining_ears
    return result

print(solution())