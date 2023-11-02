def solution():
    original_group = 200
    first_snack_group = 100
    first_newcomers = 20
    first_leaving_group = first_snack_group / 2
    second_newcomers = 10
    second_leaving_group = 30
    third_leaving_group = (first_snack_group + first_newcomers - first_leaving_group + second_newcomers - second_leaving_group) / 2
    result = third_leaving_group
    return result

print(solution())