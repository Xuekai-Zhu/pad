def solution():
    # Calculate the volume of cooked spinach
    cooked_spinach_vol = 0.2 * 40  # spinach is cooked until it's 20% of its initial volume

    # Calculate the total volume of the quiche
    total_quiche_vol = cooked_spinach_vol + 6 + 4  # spinach is mixed with cream cheese and eggs

    result = total_quiche_vol
    return result

print(solution())