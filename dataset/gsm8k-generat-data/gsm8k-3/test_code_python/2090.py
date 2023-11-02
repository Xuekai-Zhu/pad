def solution():
    """A bag full of sugar weighs 16 kg. A bag full of salt weighs 30 kg. If you remove 4 kg from the combined weight of these two bags, how much do the bags now weigh?"""
    # Define the weight of the sugar bag and the salt bag
    sugar_weight = 16
    salt_weight = 30

    # Calculate the combined weight of the bags
    combined_weight = sugar_weight + salt_weight

    # Remove 4 kg from the combined weight
    new_weight = combined_weight - 4

    # Display the new weight of the bags
    result = new_weight
    return result

print(solution())