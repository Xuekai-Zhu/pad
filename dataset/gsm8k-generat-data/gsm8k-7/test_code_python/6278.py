def solution():
    apple_slices_per_pie = 8
    peach_slices_per_pie = 6
    num_customers_apple = 56
    num_customers_peach = 48

    # Calculate the total number of apple pie slices sold
    total_apple_slices = apple_slices_per_pie * num_customers_apple

    # Calculate the total number of peach pie slices sold
    total_peach_slices = peach_slices_per_pie * num_customers_peach

    # Calculate the total number of pies sold
    total_pies = (total_apple_slices + total_peach_slices) / (apple_slices_per_pie + peach_slices_per_pie)
    result = total_pies
    return result

print(solution())