def solution():
    # Calculate the total number of ears of corn
    total_ears = 4 * 108

    # Calculate the number of ears with 500 kernels and those with 600 kernels
    half_ears = total_ears / 2
    ears_500 = half_ears
    ears_600 = half_ears

    # Calculate the total number of kernels
    total_kernels = (ears_500 * 500) + (ears_600 * 600)
    result = total_kernels
    return result

print(solution())