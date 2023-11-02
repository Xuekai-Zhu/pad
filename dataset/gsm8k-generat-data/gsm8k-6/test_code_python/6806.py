def solution(savings):
    # Calculate the number of Russian dolls Daniel can buy at the discounted price
    original_price_dolls = 4
    discounted_price_dolls = 3
    original_num_dolls = savings // original_price_dolls
    discounted_num_dolls = original_num_dolls + ((savings % original_price_dolls) // discounted_price_dolls)
    result = discounted_num_dolls
    return result

print(solution())