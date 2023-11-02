def solution():
    
    lisa_tshirts = 40
    lisa_jeans = lisa_tshirts / 2
    lisa_coats = lisa_tshirts * 2
    lisa_total = lisa_tshirts + lisa_jeans + lisa_coats

    carly_tshirts = lisa_tshirts / 4
    carly_jeans = lisa_jeans * 3
    carly_coats = lisa_coats / 4
    carly_total = carly_tshirts + carly_jeans + carly_coats

    total_spent = lisa_total + carly_total
    result = total_spent
    return result

print(solution())