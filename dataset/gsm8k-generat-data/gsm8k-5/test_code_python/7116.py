def solution():
    total_number_of_eggs = 12  # Marie makes 12 chocolate eggs
    weight_of_each_egg = 10  # Each chocolate egg weighs 10 ounces
    number_of_boxes = 4  # She packs the eggs in 4 gift boxes

    # Calculate the total weight of all the chocolate eggs
    total_weight = total_number_of_eggs * weight_of_each_egg

    # Calculate the number of eggs in each gift box
    eggs_per_box = total_number_of_eggs / number_of_boxes

    # Calculate the weight of the melted gift box
    melted_box_weight = eggs_per_box * weight_of_each_egg

    # Calculate the weight of the remaining chocolate eggs
    remaining_weight = total_weight - melted_box_weight
    result = remaining_weight
    return result

print(solution())