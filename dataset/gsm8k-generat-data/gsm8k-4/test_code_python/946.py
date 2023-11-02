def solution():
    """Ruby is taking dance lessons. They cost $75 for 10 classes in one pack. She can add additional classes at the price of 1/3 more than the average price of a class on the lesson in the pack. if she takes 13 total classes, how much does she pay?"""
    # Define the cost of a pack of 10 classes
    pack_cost = 75

    # Calculate the cost of each class in the pack
    class_cost = pack_cost / 10

    # Calculate the cost of additional classes
    extra_class_cost = class_cost * (1 + 1/3)

    # Calculate the total cost of 13 classes, including the pack and additional classes
    total_cost = pack_cost + (extra_class_cost * 3)

    # return the result
    result = total_cost
    return result

print(solution())