def solution():
    """2 tablespoons of popcorn kernels will make 4 cups of popcorn. For movie night, Joanie wants 3 cups of popcorn, Mitchell wants 4 cups of popcorn, Miles and Davis said they would split 6 cups of popcorn and Cliff said he would only eat 3 cups. How many tablespoons of popcorn kernels will they need?"""
    cups_per_kernel = 4 / 2
    total_cups = 3 + 4 + 6 + 3
    total_kernels = total_cups / cups_per_kernel
    result = total_kernels
    return result

print(solution())