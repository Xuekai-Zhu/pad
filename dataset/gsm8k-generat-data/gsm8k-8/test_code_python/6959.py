def solution():
    debelyn_start = 20
    andrena_start = 0   # let's assume Andrena didn't have any dolls to start with
    christel_start = 24

    andrena_after_debelyn_gift = andrena_start + 2
    christel_after_andrena_gift = christel_start - 5
    andrena_after_christel_gift = christel_after_andrena_gift + 2

    debelyn_end = debelyn_start - 2
    andrena_end = andrena_after_debelyn_gift + andrena_after_christel_gift
    andrena_diff = andrena_end - debelyn_end

    result = andrena_diff
    return result

print(solution())