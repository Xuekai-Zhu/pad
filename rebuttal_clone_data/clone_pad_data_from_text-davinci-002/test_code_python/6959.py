def solution():
    dolls_before_gift = 20
    dolls_given = 2
    dolls_after_gift = dolls_before_gift - dolls_given
    dolls_before_gift_2 = 24
    dolls_given_2 = 5
    dolls_after_gift_2 = dolls_before_gift_2 - dolls_given_2
    dolls_after_gift_3 = dolls_after_gift_2 + 2
    result = dolls_after_gift_3 - dolls_after_gift
    return result

print(solution())