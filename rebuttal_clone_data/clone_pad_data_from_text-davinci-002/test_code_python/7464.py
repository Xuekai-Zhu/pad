def solution():
     ears_per_stalk = 4
     stalks = 108
     ears_with_500_kernels = ears_per_stalk / 2
     ears_with_600_kernels = ears_per_stalk / 2
     kernels_per_ear_with_500_kernels = 500
     kernels_per_ear_with_600_kernels = 600
     total_kernels = (ears_with_500_kernels * kernels_per_ear_with_500_kernels) + (ears_with_600_kernels * kernels_per_ear_with_600_kernels)
     result = total_kernels
     return result

print(solution())