def solution():
    num_books = 20
    discount = 2
    base_price = 20
    total_price = 0

    for i in range(num_books):
        if i < 5:
            total_price += base_price
        else:
            total_price += max(0, base_price - (i - 4) * discount)

    result = total_price
    return result

print(solution())