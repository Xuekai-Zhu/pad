def solution():
    original_price = 500  # The bag was originally priced at $500
    first_reduction = 0.05  # The price was reduced by 5% after a week
    second_reduction = 0.04  # The selling price was reduced by 4% a month after

    # Calculate the price after the first reduction
    price_after_first_reduction = original_price - (original_price * first_reduction)

    # Calculate the price after the second reduction
    price_after_second_reduction = price_after_first_reduction - (price_after_first_reduction * second_reduction)

    # Calculate the total reduction from the original selling price
    total_reduction = original_price - price_after_second_reduction
    result = total_reduction
    return result

print(solution())