def solution():
    # Calculate Juniper's original number of bones
    original_bones = 4

    # Calculate the number of bones Juniper receives from her master
    new_bones = original_bones * 2

    # Calculate the number of bones remaining after the neighbor's dog stole 2
    remaining_bones = new_bones - 2
    result = remaining_bones
    return result

print(solution())