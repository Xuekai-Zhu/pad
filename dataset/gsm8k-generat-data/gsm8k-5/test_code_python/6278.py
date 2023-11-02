def solution():
    apple_slices_per_pie = 8  # Each apple pie is cut into 8 slices
    peach_slices_per_pie = 6  # Each peach pie is cut into 6 slices
    apple_slices_ordered = 56  # 56 customers ordered apple pie slices
    peach_slices_ordered = 48  # 48 customers ordered peach pie slices

    # Calculate the total number of apple pies sold
    apple_pies_sold = apple_slices_ordered / apple_slices_per_pie

    # Calculate the total number of peach pies sold
    peach_pies_sold = peach_slices_ordered / peach_slices_per_pie

    # Calculate the total number of pies sold
    total_pies_sold = apple_pies_sold + peach_pies_sold
    result = total_pies_sold
    return result

print(solution())