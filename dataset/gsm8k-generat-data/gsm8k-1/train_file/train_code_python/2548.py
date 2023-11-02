def solution():
    """A blacksmith has 400kg of iron to make horseshoes for neighbouring farms and stables. There are 2 farms nearby, each of which has 2 horses. There are 2 stables nearby which all have 5 horses each. While the blacksmith is crafting, a riding school reaches out and asks for as many horseshoes as possible for their own horses. The blacksmith promises to give them however many horseshoes he has left when he has finished his orders for the farms and stables. If each horseshoe needs 2kg of iron, how many horses will get new horseshoes at the riding school?"""
    iron_available = 400
    iron_per_horseshoe = 2
    total_horseshoes_possible = iron_available / iron_per_horseshoe

    farms_horses = 2 * 2
    stables_horses = 2 * 5
    total_horses_to_shoe = farms_horses + stables_horses

    horseshoes_used = total_horses_to_shoe * 4  # each horse needs 4 horseshoes
    horseshoes_left = total_horseshoes_possible - horseshoes_used

    riding_school_horses = horseshoes_left / 4  # each horse needs 4 horseshoes
    result = riding_school_horses
    return result

print(solution())