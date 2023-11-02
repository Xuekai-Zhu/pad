def solution():
    # Calculate the amount of iron needed for the farms
    iron_farms = 2 * 2 * 4 * 2  # 2 farms, 2 horses per farm, 4 horseshoes per horse, 2kg of iron per horseshoe

    # Calculate the amount of iron needed for the stables
    iron_stables = 2 * 5 * 4 * 2  # 2 stables, 5 horses per stable, 4 horseshoes per horse, 2kg of iron per horseshoe

    # Calculate the total amount of iron used for the farms and stables
    total_iron = iron_farms + iron_stables

    # Calculate the remaining iron for the riding school
    remaining_iron = 400 - total_iron

    # Calculate the number of horseshoes that can be made with the remaining iron
    remaining_horseshoes = remaining_iron / 2

    # Calculate the number of horses at the riding school that can get new horseshoes
    horses_with_new_horseshoes = remaining_horseshoes / 4

    result = horses_with_new_horseshoes
    return result

print(solution())