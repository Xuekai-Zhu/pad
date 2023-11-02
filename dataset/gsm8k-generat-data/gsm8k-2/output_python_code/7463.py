def solution():
    """Hilary is shucking corn from ears that grew on her farm. She gets four ears of corn per stalk, and she has 108 stalks growing. Half the ears of corn have 500 kernels of corn and the other half have 100 more. How many kernels of corn does Hilary have to shuck?"""
    ears_per_stalk = 4
    total_stalks = 108
    half_with_500 = (total_stalks * ears_per_stalk) / 2
    half_with_600 = (total_stalks * ears_per_stalk) / 2
    total_kernels = (half_with_500 * 500) + (half_with_600 * 600)
    result = total_kernels
    return result

print(solution())