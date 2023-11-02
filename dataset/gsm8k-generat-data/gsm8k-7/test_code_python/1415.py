def solution():
    price_per_slice = 7
    slices_per_cheesecake = 6
    num_cheesecakes = 7

    # Calculate the total number of slices of cheesecake sold
    total_slices = num_cheesecakes * slices_per_cheesecake

    # Calculate the total amount of money made from selling all the cheesecake
    total_money = total_slices * price_per_slice
    result = total_money
    return result

print(solution())