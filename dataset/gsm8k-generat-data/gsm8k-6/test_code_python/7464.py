def solution():
    # Find the total number of ears of corn
    total_corn_ears = 4 * 108  # 4 ears of corn per stalk, 108 stalks growing

    # Find the number of ears with 500 kernels and the number with 600 kernels
    ears_with_500_kernels = total_corn_ears / 2
    ears_with_600_kernels = total_corn_ears / 2

    # Calculate the total number of kernels of corn
    total_kernels = (ears_with_500_kernels * 500) + (ears_with_600_kernels * 600)

    result = total_kernels
    return result

print(solution())