def solution():
    """A group of 30 tourists sets out on a walking tour of the rainforest. Two tourists are eaten by anacondas, then half the remaining tourists try to pet poisonous dart frogs and get poisoned. If only 1/7 of the poisoned tourists recovered, how many tourists are left at the end of the tour?"""
    total_tourists = 30
    anaconda_victims = 2
    remaining_tourists = total_tourists - anaconda_victims
    poisoned_tourists = remaining_tourists // 2
    recovered_tourists = poisoned_tourists // 7
    remaining_tourists = remaining_tourists - poisoned_tourists + recovered_tourists
    result = remaining_tourists
    return result

print(solution())