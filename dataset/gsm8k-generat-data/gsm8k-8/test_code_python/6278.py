def solution():
    # Calculate the total number of apple pie slices sold
    apple_slices_sold = 56 * 8

    # Calculate the total number of peach pie slices sold
    peach_slices_sold = 48 * 6

    # Calculate the total number of pies sold
    pies_sold = (apple_slices_sold + peach_slices_sold) / 8

    result = pies_sold
    return result

print(solution())