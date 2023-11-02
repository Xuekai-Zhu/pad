def solution():
    num_choco_ice_creams = 50
    num_mango_ice_creams = 54

    # Calculate the number of chocolate ice creams sold
    num_choco_sold = int(num_choco_ice_creams * 3/5)

    # Calculate the number of mango ice creams sold
    num_mango_sold = int(num_mango_ice_creams * 2/3)

    # Calculate the total number of ice creams sold
    total_sold = num_choco_sold + num_mango_sold

    # Calculate the total number of ice creams not sold
    total_not_sold = (num_choco_ice_creams + num_mango_ice_creams) - total_sold
    result = total_not_sold
    return result

print(solution())