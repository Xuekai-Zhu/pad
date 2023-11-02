def solution():
    
    ears_per_stalk = 4
    total_stalks = 108
    half_with_500 = (total_stalks * ears_per_stalk) / 2
    half_with_600 = (total_stalks * ears_per_stalk) / 2
    total_kernels = (half_with_500 * 500) + (half_with_600 * 600)
    result = total_kernels
    return result

print(solution())