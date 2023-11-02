def solution():
    ears_per_stalk = 4  # Hilary gets 4 ears of corn per stalk
    num_stalks = 108  # Hilary has 108 stalks growing
    total_ears = ears_per_stalk * num_stalks  # Calculate the total number of ears

    # Calculate the number of ears with 500 kernels and with 600 kernels
    half_ears = total_ears // 2
    num_500_kernel_ears = half_ears
    num_600_kernel_ears = total_ears - half_ears

    # Calculate the total number of kernels of corn
    total_kernels = (num_500_kernel_ears * 500) + (num_600_kernel_ears * 600)
    result = total_kernels
    return result

print(solution())