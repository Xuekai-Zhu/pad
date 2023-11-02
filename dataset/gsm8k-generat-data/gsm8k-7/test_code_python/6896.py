def solution():
    num_apples = 15
    apple_price = 2
    num_grapes = 12
    grape_price = 1.5

    # Calculate the total earnings from selling candied apples
    apple_earnings = num_apples * apple_price

    # Calculate the total earnings from selling candied grapes
    grape_earnings = num_grapes * grape_price

    # Calculate the total earnings from selling everything
    total_earnings = apple_earnings + grape_earnings
    result = total_earnings
    return result

print(solution())