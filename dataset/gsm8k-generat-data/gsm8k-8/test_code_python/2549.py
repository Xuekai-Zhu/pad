def solution():
    # Calculate the amount of iron needed for the farms and stables
    iron_for_farms = 2 * 2 * 4 * 2  # 2 farms, 2 horses each farm, 4 horseshoes per horse, 2kg per horseshoe
    iron_for_stables = 2 * 5 * 4 * 2  # 2 stables, 5 horses each stable, 4 horseshoes per horse, 2kg per horseshoe
    total_iron_for_orders = iron_for_farms + iron_for_stables

    # Calculate the number of horseshoes that can be made with the remaining iron
    remaining_iron = 400 - total_iron_for_orders
    remaining_horseshoes = remaining_iron // 2

    # Calculate the number of horses that can be shoed at the riding school
    horses_at_riding_school = remaining_horseshoes // 4

    result = horses_at_riding_school
    return result

print(solution())