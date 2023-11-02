def solution():
    # Calculate the total weight of the meatballs
    total_weight = 4

    # Calculate the number of meatballs that can be made
    num_meatballs = total_weight / (1 / 8)

    # Calculate the number of meatballs each family member will eat (including Antonio)
    num_per_person = num_meatballs / 8

    # Calculate the number of meatballs Antonio will eat
    antonio_num = num_per_person * 2  # Antonio is counted as two people since he is preparing the meal

    result = antonio_num
    return result

print(solution())