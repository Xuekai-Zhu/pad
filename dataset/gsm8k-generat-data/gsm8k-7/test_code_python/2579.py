def solution():
    num_boxes = 4
    num_crayons_per_box = 8
    num_crayons_given_to_mae = 5
    num_crayons_left = 15

    # Calculate the total number of crayons Nori had
    total_crayons = num_boxes * num_crayons_per_box

    # Calculate the total number of crayons she gave away
    total_crayons_given_away = num_crayons_given_to_mae + (total_crayons - num_crayons_left)

    # Calculate the number of crayons given to Lea
    num_crayons_given_to_lea = total_crayons_given_away - num_crayons_given_to_mae

    # Calculate the difference between the number of crayons given to Lea and Mae
    difference = num_crayons_given_to_lea - num_crayons_given_to_mae
    result = difference
    return result

print(solution())