def solution():
    # Number of hairs washed down the drain while washing hair
    wash_hairs = 32

    # Number of hairs brushed out after washing
    brush_hairs = wash_hairs / 2

    # Total number of hairs lost after washing and brushing
    total_hairs_lost = wash_hairs + brush_hairs

    # Number of hairs that Anya needs to grow back to always have one more hair than she started with
    hairs_to_grow_back = total_hairs_lost + 1

    result = hairs_to_grow_back
    return result

print(solution())