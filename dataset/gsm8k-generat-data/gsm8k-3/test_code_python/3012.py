def solution():
    """Amber is baking cakes for her party. She has invited 8 friends and each one will want two slices of cake. Each cake makes 6 slices. If she bakes 4 cakes, how many slices will be left over at the end if she eats three herself?"""
    # Define the number of friends and slices per cake
    FRIENDS = 8
    SLICES_PER_CAKE = 6

    # Calculate the total number of slices needed
    slices_needed = FRIENDS * 2

    # Calculate the total number of slices from 4 cakes
    total_slices = 4 * SLICES_PER_CAKE

    # Subtract 3 slices for Amber
    total_slices -= 3

    # Calculate the number of leftover slices
    leftovers = total_slices - slices_needed

    # Display the number of leftover slices
    result = leftovers
    return result

print(solution())