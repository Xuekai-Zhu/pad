def solution():
    original_cost = 500  # wears originally cost $500
    additional_cost = (2/5) * original_cost  # Mrs. Smith needs two-fifths more money than she had
    total_cost = original_cost + additional_cost  # total cost of wears
    discounted_cost = total_cost - 0.15 * total_cost  # discounted cost after 15% discount
    remaining_cost = discounted_cost - original_cost  # remaining amount Mrs. Smith still needs to pay
    result = remaining_cost
    return result

print(solution())