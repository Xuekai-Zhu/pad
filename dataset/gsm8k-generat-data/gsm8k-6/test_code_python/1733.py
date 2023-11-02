def solution():
    # Calculate the initial number of clothes Adam has
    initial_clothes = 4 + 4 + (4*2) + 20  # 4 pants, 4 jumpers, 4 pajama sets (top and bottom), and 20 t-shirts

    # Calculate the number of clothes Adam is keeping after the cleanup
    clothes_kept = initial_clothes / 2

    # Calculate the total number of clothes donated by Adam and his friends
    total_donated = initial_clothes - clothes_kept + (3 * initial_clothes)

    result = total_donated
    return result

print(solution())