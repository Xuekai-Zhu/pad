def solution():
    batch_size = 48
    chocolate_chips = 108
    mms = chocolate_chips / 3
    total_chocolate = chocolate_chips + mms
    average_per_cookie = total_chocolate / batch_size
    result = average_per_cookie
    return result

print(solution())