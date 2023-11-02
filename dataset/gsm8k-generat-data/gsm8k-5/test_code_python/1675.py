def solution():
    empty_weight = 500  # The lorry weighs 500 pounds when empty
    bag_weight = 60  # Each bag of apples weighs 60 pounds
    num_bags = 20  # There are 20 bags of apples loaded onto the lorry

    # Calculate the total weight of the loaded lorry
    loaded_weight = empty_weight + (bag_weight * num_bags)
    result = loaded_weight
    return result

print(solution())