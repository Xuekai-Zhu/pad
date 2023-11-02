def solution():
    # Calculate the number of apple and peach pies sold by Milton
    apple_pie_slices = 56  # 56 customers ordered apple pie slices
    peach_pie_slices = 48  # 48 customers ordered peach pie slices
    apple_pies = apple_pie_slices / 8  # Milton cuts the apple pie into 8 slices
    peach_pies = peach_pie_slices / 6  # Milton cuts the peach pie into 6 slices
    total_pies = apple_pies + peach_pies  # calculate the total number of pies sold by Milton
    result = total_pies
    return result

print(solution())