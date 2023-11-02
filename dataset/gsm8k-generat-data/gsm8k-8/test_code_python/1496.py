def solution():
    # Define Juniper's starting number of bones
    juniper_bones = 4

    # Double Juniper's number of bones
    juniper_bones = juniper_bones * 2

    # Subtract two bones stolen by neighbor's dog
    juniper_bones = juniper_bones - 2

    result = juniper_bones
    return result

print(solution())