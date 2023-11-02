def solution():
    # Find the size of the guest bedroom and the combined size of the living room, dining room and kitchen
    guest_bedroom = (1/5) * (2300 - 1000)  # guest bedroom is 1/4 the size of the master bedroom suite
    ldk = 1000  # living room, dining room and kitchen combined take up 1,000 sq ft

    # Calculate the size of the master bedroom suite
    master_suite = 2300 - guest_bedroom - ldk
    result = master_suite
    return result

print(solution())