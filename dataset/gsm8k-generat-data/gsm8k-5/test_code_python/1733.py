def solution():
    # Calculate the total number of clothes Adam started with
    total_starting_clothes = (4 * 2) + 4 + (4 * 2) + 20  # 4 pairs of pants (each is 2 pieces), 4 jumpers, 4 pajama sets (each is 2 pieces), and 20 t-shirts

    # Calculate the number of clothes Adam wants to keep
    clothes_to_keep = total_starting_clothes / 2

    # Calculate the total number of clothes Adam and his friends donated
    donated_clothes = (4 * 2) + 4 + (4 * 2) + 20  # Same amount as Adam

    # Calculate the total number of clothes donated including Adam's contribution
    total_donated_clothes = (donated_clothes * 4) + total_starting_clothes - clothes_to_keep

    result = total_donated_clothes
    return result

print(solution())