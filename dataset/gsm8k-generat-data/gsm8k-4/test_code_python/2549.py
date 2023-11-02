def solution():
    """A blacksmith has 400kg of iron to make horseshoes for neighbouring farms and stables. There are 2 farms nearby, each of which has 2 horses. There are 2 stables nearby which all have 5 horses each. While the blacksmith is crafting, a riding school reaches out and asks for as many horseshoes as possible for their own horses. The blacksmith promises to give them however many horseshoes he has left when he has finished his orders for the farms and stables. If each horseshoe needs 2kg of iron, how many horses will get new horseshoes at the riding school?"""
    # Define the weight of iron needed to make one horseshoe
    IRON_PER_SHOE = 2

    # Calculate the total weight of iron needed for the farms and stables
    farms_horses = 2 * 2
    stables_horses = 2 * 5
    total_horses = farms_horses + stables_horses
    iron_needed = total_horses * IRON_PER_SHOE

    # Calculate the weight of iron left for the riding school
    iron_left = 400 - iron_needed

    # Calculate the number of horseshoes that can be made with the remaining iron
    horseshoes_left = iron_left / IRON_PER_SHOE

    # Calculate the number of horses that can get new horseshoes at the riding school
    riding_school_horses = int(horseshoes_left / 4)

    # Return the result
    result = riding_school_horses
    return result

print(solution())