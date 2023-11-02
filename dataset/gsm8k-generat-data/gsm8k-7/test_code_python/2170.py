def solution():
    barrettes_price = 3
    comb_price = 1

    # Kristine buys one set of barrettes and one comb
    kristine_total = barrettes_price + comb_price

    # Crystal buys three sets of barrettes and one comb
    crystal_total = (3 * barrettes_price) + comb_price

    # Calculate the total amount spent by both girls
    total_spent = kristine_total + crystal_total
    result = total_spent
    return result

print(solution())