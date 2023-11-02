def solution():
    # Convert the total amount of fluffy foam material to pounds
    total_material = 3 * 2000

    # Calculate the amount of foam material needed per pillow
    material_per_pillow = 5 - 3

    # Calculate how many pillows Teddy can make with the total amount of material
    num_pillows = total_material // material_per_pillow

    result = num_pillows
    return result

print(solution())