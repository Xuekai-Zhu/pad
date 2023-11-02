def solution():
    """A house’s living room, dining room and kitchen take up 1,000 sq ft. The house also has a guest bedroom and a master bedroom suite. If the guest bedroom is a quarter of the size of the master bedroom suite, and the house is 2,300 sq ft total, how large is the master bedroom suite?"""
    living_dining_kitchen = 1000
    total_size = 2300
    guest_bedroom = total_size - living_dining_kitchen
    master_bedroom = 4 * guest_bedroom
    result = master_bedroom
    return result

print(solution())