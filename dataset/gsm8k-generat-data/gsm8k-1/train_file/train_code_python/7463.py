def solution():
    """Hilary is shucking corn from ears that grew on her farm. She gets four ears of corn per stalk, and she has 108 stalks growing. Half the ears of corn have 500 kernels of corn and the other half have 100 more. How many kernels of corn does Hilary have to shuck?"""
    ears_per_stalk = 4
    num_stalks = 108
    total_ears = ears_per_stalk * num_stalks
    half_of_ears = total_ears / 2
    # calculate the number of ears with 500 kernels of corn
    ears_with_500_kernels = half_of_ears
    # calculate the number of ears with 600 kernels of corn
    ears_with_600_kernels = half_of_ears
    total_kernels = (ears_with_500_kernels * 500) + (ears_with_600_kernels * 600)
    result = total_kernels
    return result

print(solution())