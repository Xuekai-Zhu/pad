def solution():
    """A house’s living room, dining room and kitchen take up 1,000 sq ft. The house also has a guest bedroom and a master bedroom suite. If the guest bedroom is a quarter of the size of the master bedroom suite, and the house is 2,300 sq ft total, how large is the master bedroom suite?"""
    total_size = 2300
    living_size = 1000
    guest_size = (1/5) * (total_size - living_size)
    master_size = total_size - living_size - guest_size
    result = master_size
    return result

print(solution())