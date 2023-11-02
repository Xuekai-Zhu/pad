def solution():
    """Hilary is shucking corn from ears that grew on her farm. She gets four ears of corn per stalk, and she has 108 stalks growing. Half the ears of corn have 500 kernels of corn and the other half have 100 more. How many kernels of corn does Hilary have to shuck?"""
    # Define the number of stalks and ears per stalk
    stalks = 108
    ears_per_stalk = 4

    # Calculate the total number of ears
    total_ears = stalks * ears_per_stalk

    # Calculate the number of ears with 500 kernels and with 600 kernels
    half_ears = total_ears / 2
    ears_500_kernels = half_ears
    ears_600_kernels = half_ears

    # Calculate the total number of kernels
    total_kernels = (ears_500_kernels * 500) + (ears_600_kernels * 600)

    result = total_kernels
    return result

print(solution())