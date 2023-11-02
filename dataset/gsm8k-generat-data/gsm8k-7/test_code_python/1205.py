def solution():
    num_skeletons = 20
    num_adult_women = num_skeletons // 2
    num_adult_men = (num_skeletons - num_adult_women) // 2
    num_children = num_skeletons - num_adult_women - num_adult_men

    # Calculate the total number of bones in adult women
    bones_per_adult_woman = 20
    total_bones_adult_women = num_adult_women * bones_per_adult_woman

    # Calculate the total number of bones in adult men
    bones_per_adult_man = bones_per_adult_woman + 5
    total_bones_adult_men = num_adult_men * bones_per_adult_man

    # Calculate the total number of bones in children
    bones_per_child = bones_per_adult_woman / 2
    total_bones_children = num_children * bones_per_child

    # Calculate the total number of bones in the graveyard
    total_bones_graveyard = total_bones_adult_women + total_bones_adult_men + total_bones_children
    result = total_bones_graveyard
    return result

print(solution())