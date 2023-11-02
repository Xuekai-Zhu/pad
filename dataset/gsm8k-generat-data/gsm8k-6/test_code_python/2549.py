def solution():
    # Calculate the total number of horseshoes that can be made with 400kg of iron
    total_horseshoes = 400 // 2  # each horseshoe needs 2kg of iron

    # Calculate the number of horses in the farms and stables
    num_horses_in_farms = 2 * 2  # 2 farms with 2 horses each
    num_horses_in_stables = 2 * 5  # 2 stables with 5 horses each
    total_horses = num_horses_in_farms + num_horses_in_stables

    # Calculate the number of horseshoes needed for the farms and stables
    horseshoes_for_farms_and_stables = total_horses * 4  # each horse needs 4 horseshoes

    # Calculate the number of horseshoes left for the riding school
    horseshoes_left = total_horseshoes - horseshoes_for_farms_and_stables
    num_horses_at_riding_school = horseshoes_left // 4  # each horse needs 4 horseshoes

    result = num_horses_at_riding_school
    return result

print(solution())