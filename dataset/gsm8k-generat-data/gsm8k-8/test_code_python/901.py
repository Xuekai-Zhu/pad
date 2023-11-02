def solution():
    sandi_spent = 600 / 2
    gillian_spent = 150 + 3 * sandi_spent
    result = gillian_spent - sandi_spent
    return result

print(solution())