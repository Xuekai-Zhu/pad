def solution():
    ears_per_stalk = 4
    num_stalks = 108
    half_with_500_kernels = (ears_per_stalk * num_stalks) / 2
    half_with_600_kernels = (ears_per_stalk * num_stalks) / 2
    total_kernels = (half_with_500_kernels * 500) + (half_with_600_kernels * 600)
    result = total_kernels
    return result

print(solution())