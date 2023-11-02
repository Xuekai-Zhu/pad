def solution():
    original_price = 4
    discounted_price = 3
    num_dolls_saved_for = 15

    # Calculate how many dolls Daniel could have bought at the original price
    num_dolls_original = num_dolls_saved_for / original_price

    # Calculate how much money Daniel saved for the dolls
    total_saved = num_dolls_saved_for * original_price

    # Calculate how many dolls he can buy at the discounted price with his savings
    num_dolls_discounted = total_saved / discounted_price
    result = num_dolls_discounted
    return result

print(solution())