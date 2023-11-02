def solution():
    """A bag full of sugar weighs 16 kg. A bag full of salt weighs 30 kg. If you remove 4 kg from the combined weight of these two bags, how much do the bags now weigh?"""
    # Define the weights of the bags
    sugar_weight = 16
    salt_weight = 30

    # Calculate the total weight before removing 4 kg
    total_weight = sugar_weight + salt_weight

    # Subtract 4 kg from the total weight
    total_weight -= 4

    # return the result
    result = total_weight
    return result

print(solution())