def solution():
    """To raise funds for her local soup kitchen, Didi enlisted the help of her family, friends, and neighbors. They donated 10 same-size cakes that she sliced into 8 slices per cake and started selling a slice for $1. A local business owner was so impressed by Didi's efforts that she offered to donate 50 cents for each slice Didi sold. A second business owner also offered to donate a quarter for each slice sold. If Didi sold all the slices, how much money did she raise?"""
    num_cakes = 10
    slices_per_cake = 8
    price_per_slice = 1
    donation_per_slice_1 = 0.5
    donation_per_slice_2 = 0.25
    
    total_slices = num_cakes * slices_per_cake
    money_raised = total_slices * price_per_slice
    donation_1 = total_slices * donation_per_slice_1
    donation_2 = total_slices * donation_per_slice_2
    
    total_money_raised = money_raised + donation_1 + donation_2
    result = total_money_raised
    
    return result

print(solution())