def solution():
    """A blacksmith has 400kg of iron to make horseshoes for neighbouring farms and stables. There are 2 farms nearby, each of which has 2 horses. There are 2 stables nearby which all have 5 horses each. While the blacksmith is crafting, a riding school reaches out and asks for as many horseshoes as possible for their own horses. The blacksmith promises to give them however many horseshoes he has left when he has finished his orders for the farms and stables. If each horseshoe needs 2kg of iron, how many horses will get new horseshoes at the riding school?"""
    iron_available = 400
    horseshoe_iron = 2
    total_horseshoes = iron_available // horseshoe_iron
    total_horses_farms = 2 * 2 * 2
    total_horses_stables = 2 * 5 * 2
    horseshoes_farms_stables = total_horses_farms + total_horses_stables
    remaining_horseshoes = total_horseshoes - horseshoes_farms_stables
    horseshoes_riding_school = remaining_horseshoes
    horses_riding_school = horseshoes_riding_school // 4
    result = horses_riding_school
    return result

print(solution())