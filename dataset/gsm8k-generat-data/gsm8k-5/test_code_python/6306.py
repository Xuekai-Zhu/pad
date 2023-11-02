def solution():
    apples_weight = 4  # Each apple weighs 4 ounces
    oranges_weight = 3  # Each orange weighs 3 ounces
    bag_capacity = 49  # Each plastic bag can hold 49 ounces of fruit
    full_bags = 3  # Marta wants to buy 3 full bags of fruit

    # Calculate the number of apples and oranges in each bag
    total_fruit_per_bag = bag_capacity / 2  # Marta wants to put an equal number of apples and oranges in each bag
    apples_and_oranges_per_bag = total_fruit_per_bag / (apples_weight + oranges_weight)
    apples_per_bag = oranges_per_bag = apples_and_oranges_per_bag / 2

    # Calculate the total weight of apples Marta needs to buy
    total_apples_weight = apples_per_bag * full_bags * bag_capacity / 2
    result = total_apples_weight
    return result

print(solution())