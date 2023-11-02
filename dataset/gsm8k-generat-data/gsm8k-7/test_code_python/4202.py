def solution():
    total_time = 2 * 60  # in minutes
    bake_time = 15
    icing_time = 30 * 2

    prep_time = total_time - bake_time - icing_time

    result = prep_time
    return result

print(solution())