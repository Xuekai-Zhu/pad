def solution():
    quarters = 14  # Winston has 14 quarters
    half_dollar = 50  # Half a dollar is worth 50 cents
    spent_on_candy = half_dollar / 2  # Winston spends half a dollar on candy

    # Calculate the total amount Winston has left in cents
    total_cents = (quarters * 25) + (half_dollar - spent_on_candy)
    result = total_cents
    return result

print(solution())