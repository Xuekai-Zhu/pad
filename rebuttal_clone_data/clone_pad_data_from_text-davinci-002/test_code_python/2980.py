def solution():
    bowls_bought = 20 * 20
    bowls_given_away = bowls_bought / 10 * 2
    bowls_remaining = 70 - bowls_given_away
    result = bowls_remaining
    return result

print(solution())