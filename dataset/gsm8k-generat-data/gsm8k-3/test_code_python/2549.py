def solution():
    """A blacksmith has 400kg of iron to make horseshoes for neighbouring farms and stables. There are 2 farms nearby, each of which has 2 horses. There are 2 stables nearby which all have 5 horses each. While the blacksmith is crafting, a riding school reaches out and asks for as many horseshoes as possible for their own horses. The blacksmith promises to give them however many horseshoes he has left when he has finished his orders for the farms and stables. If each horseshoe needs 2kg of iron, how many horses will get new horseshoes at the riding school?"""
    # Define the amount of iron needed per horseshoe
    IRON_PER_HORSESHOE = 2

    # Define the number of horses at each farm and stable
    farm_horses = 2
    stable_horses = 5

    # Calculate the total number of horses that need horseshoes
    total_horses = 2 * farm_horses + 2 * stable_horses

    # Calculate the total amount of iron needed for all the horseshoes
    total_iron_needed = total_horses * IRON_PER_HORSESHOE

    # Calculate the amount of iron left over for the riding school
    iron_left_over = 400 - total_iron_needed

    # Calculate the number of horseshoes that can be made with the remaining iron
    horseshoes_left_over = iron_left_over // IRON_PER_HORSESHOE

    # Calculate the number of horses at the riding school that can receive new horseshoes
    horses_with_new_horseshoes = horseshoes_left_over // 4

    # Display the number of horses at the riding school with new horseshoes
    result = horses_with_new_horseshoes
    return result

print(solution())