def solution():
    """A bag full of sugar weighs 16 kg. A bag full of salt weighs 30 kg. If you remove 4 kg from the combined weight of these two bags, how much do the bags now weigh?"""
    sugar_weight = 16
    salt_weight = 30
    combined_weight = sugar_weight + salt_weight
    new_combined_weight = combined_weight - 4
    result = new_combined_weight
    return result

print(solution())