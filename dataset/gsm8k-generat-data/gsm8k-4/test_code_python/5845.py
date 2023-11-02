def solution():
    """To raise funds for her local soup kitchen, Didi enlisted the help of her family, friends, and neighbors. They donated 10 same-size cakes that she sliced into 8 slices per cake and started selling a slice for $1. A local business owner was so impressed by Didi's efforts that she offered to donate 50 cents for each slice Didi sold. A second business owner also offered to donate a quarter for each slice sold. If Didi sold all the slices, how much money did she raise?"""
    
    # Define the number of cakes and slices
    num_cakes = 10
    slices_per_cake = 8
    total_slices = num_cakes * slices_per_cake

    # Define the cost per slice and the donation amounts
    cost_per_slice = 1
    donation1_per_slice = 0.5
    donation2_per_slice = 0.25

    # Calculate the total amount raised
    total_raised = total_slices * cost_per_slice + total_slices * donation1_per_slice + total_slices * donation2_per_slice

    result = total_raised
    return result

print(solution())