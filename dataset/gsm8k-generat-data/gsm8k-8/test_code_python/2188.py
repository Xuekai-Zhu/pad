def solution():
    # Calculate the total weight of the 2 larger antacids
    total_weight_larger = 2 * 2

    # Calculate the weight of zinc in the larger antacids
    zinc_larger = total_weight_larger * 0.05

    # Calculate the total weight of the 3 smaller antacids
    total_weight_smaller = 3 * 1

    # Calculate the weight of zinc in the smaller antacids
    zinc_smaller = total_weight_smaller * 0.15

    # Convert total zinc to milligrams and sum the zinc from both sets of antacids
    total_zinc_mg = (zinc_larger + zinc_smaller) * 1000
    result = total_zinc_mg
    return result

print(solution())