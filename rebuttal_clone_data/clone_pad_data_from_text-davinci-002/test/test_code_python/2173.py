def solution():
    distance_to_school = 5000
    kernels_per_foot = 1/25
    total_kernels = distance_to_school * kernels_per_foot
    eaten_by_squirrel = total_kernels * 0.25
    remaining_kernels = total_kernels - eaten_by_squirrel
    result = remaining_kernels
    return result

print(solution())