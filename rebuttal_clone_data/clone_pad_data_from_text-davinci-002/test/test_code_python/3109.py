def solution():
    scheme_a = 300
    scheme_b = 200
    percent_a = 30
    percent_b = 50
    amount_a = scheme_a + (scheme_a * (percent_a / 100))
    amount_b = scheme_b + (scheme_b * (percent_b / 100))
    difference = amount_a - amount_b
    result = difference
    return result

print(solution())