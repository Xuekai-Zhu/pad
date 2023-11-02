def solution():
    num_bones = 4
    num_additional_bones = num_bones

    # Double the number of Juniper's bones
    num_bones *= 2

    # Subtract 2 bones stolen by neighbor's dog
    num_bones -= 2

    result = num_bones
    return result

print(solution())