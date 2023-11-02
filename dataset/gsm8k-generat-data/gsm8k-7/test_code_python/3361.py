def solution():
    agnes_age = 25
    jane_age = 6
    years = 0

    while agnes_age != 2*jane_age:
        agnes_age += 1
        jane_age += 1
        years += 1

    result = years
    return result

print(solution())