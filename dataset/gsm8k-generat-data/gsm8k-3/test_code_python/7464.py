def solution():
    """Hilary is shucking corn from ears that grew on her farm. She gets four ears of corn per stalk, and she has 108 stalks growing. Half the ears of corn have 500 kernels of corn and the other half have 100 more. How many kernels of corn does Hilary have to shuck?"""
    # Calculate the total number of ears of corn
    total_ears = 4 * 108

    # Determine the number of ears with 500 kernels and the number with 600 kernels
    half_ears = total_ears // 2
    ears_with_500_kernels = half_ears
    ears_with_600_kernels = total_ears - half_ears

    # Calculate the total number of kernels
    total_kernels = (ears_with_500_kernels * 500) + (ears_with_600_kernels * 600)

    # Display the total number of kernels
    result = total_kernels
    return result

print(solution())