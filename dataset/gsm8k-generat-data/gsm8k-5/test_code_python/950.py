def solution():
    # Calculate the total earnings from stone statues
    stone_earnings = 10 * 20  # 10 stone statues at $20 each

    # Calculate the total earnings from wooden statues
    wooden_earnings = 20 * 5  # 20 wooden statues at $5 each

    # Calculate the total earnings before taxes
    total_earnings = stone_earnings + wooden_earnings

    # Calculate the tax amount
    tax_amount = 0.1 * total_earnings

    # Calculate the total earnings after taxes
    earnings_after_tax = total_earnings - tax_amount
    result = earnings_after_tax
    return result

print(solution())