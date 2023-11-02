def solution():
    lisa_shirts = 40
    lisa_jeans = lisa_shirts/2
    lisa_coats = lisa_shirts*2
    carly_shirts = lisa_shirts/4
    carly_jeans = 3*lisa_jeans
    carly_coats = lisa_coats/4

    lisa_total = lisa_shirts + lisa_jeans + lisa_coats
    carly_total = carly_shirts + carly_jeans + carly_coats

    total_spent = lisa_total + carly_total
    result = total_spent
    return result

print(solution())