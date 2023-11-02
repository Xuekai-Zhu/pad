def solution():
    total_chickens = 383

    # Let's use equations to solve the problem
    # q = 2s + 25
    # s = 3c - 4
    # q + s + c = total_chickens

    # Substituting for s in terms of c and q in terms of s
    # q = 2(3c-4) + 25
    # q = 6c + 17
    # q + (3c-4) + c = total_chickens
    # 10c + 13 = total_chickens
    # c = (total_chickens - 13) / 10

    num_colten_chickens = (total_chickens - 13) / 10
    result = num_colten_chickens
    return result

print(solution())