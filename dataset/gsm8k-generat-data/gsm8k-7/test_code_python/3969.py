def solution():
    num_As = 10
    num_Bs = 12
    num_Cs = 14
    num_Ds = 5

    extra_recess_per_A = 2
    extra_recess_per_B = 1
    extra_recess_per_C = 0
    less_recess_per_D = -1

    total_recess = 20 * (num_As + num_Bs + num_Cs + num_Ds)  # start with base recess time

    total_recess += num_As * extra_recess_per_A
    total_recess += num_Bs * extra_recess_per_B
    total_recess += num_Ds * less_recess_per_D

    result = total_recess
    return result

print(solution())