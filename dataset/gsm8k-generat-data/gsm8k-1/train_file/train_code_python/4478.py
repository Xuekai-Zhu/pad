def solution():
    """Bob grew corn in his garden this year and ended up with 50 bushels. This is way too much for him to eat, so he gave some of it away to his friends. His friend Terry took 8 bushels, while Jerry only took 3. He gave 12 bushels to his friend Linda, who runs a food pantry. His neighbor Stacy doesn't eat much corn, but she still accepted 21 ears of corn from him. If each bushel contained 14 ears of corn, how many ears of corn does Bob have left?"""
    total_bushels = 50
    terry_bushels = 8
    jerry_bushels = 3
    linda_bushels = 12
    total_given_away = terry_bushels + jerry_bushels + linda_bushels
    remaining_bushels = total_bushels - total_given_away
    ears_per_bushel = 14
    total_ears = ears_per_bushel * remaining_bushels + 21
    result = total_ears
    return result

print(solution())