def solution():
    """To raise funds for her local soup kitchen, Didi enlisted the help of her family, friends, and neighbors. They donated 10 same-size cakes that she sliced into 8 slices per cake and started selling a slice for $1. A local business owner was so impressed by Didi's efforts that she offered to donate 50 cents for each slice Didi sold. A second business owner also offered to donate a quarter for each slice sold. If Didi sold all the slices, how much money did she raise?"""
    # Define the number of cakes donated and slices per cake
    CAKES_DONATED = 10
    SLICES_PER_CAKE = 8

    # Calculate the total number of slices
    total_slices = CAKES_DONATED * SLICES_PER_CAKE

    # Calculate Didi's earnings from selling slices
    earnings = total_slices * 1

    # Calculate the first business owner's donation
    donation_1 = total_slices * 0.5

    # Calculate the second business owner's donation
    donation_2 = total_slices * 0.25

    # Calculate the total amount raised
    total_raised = earnings + donation_1 + donation_2

    # Display the total amount raised
    result = total_raised
    return result

print(solution())