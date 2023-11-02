def solution():
    classes_in_pack = 10  # There are 10 classes in one pack
    pack_price = 75  # The pack costs $75
    additional_classes = 3  # Ruby can take additional classes at 1/3 more than the average price of a class in the pack
    total_classes = 13  # Ruby will be taking a total of 13 classes

    # Calculate the average price of a class in the pack
    average_price = pack_price / classes_in_pack

    # Calculate the price of additional classes
    additional_price = additional_classes * average_price

    # Calculate the total cost of all classes
    total_cost = pack_price + (additional_price * (total_classes - classes_in_pack))

    result = total_cost
    return result

print(solution())