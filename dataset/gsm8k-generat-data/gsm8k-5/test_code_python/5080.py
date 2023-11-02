def solution():
    kimmie_earnings = 450  # Kimmie earned $450 from her handmade crafts
    zahra_earnings = kimmie_earnings * (2/3)  # Zahra earned 1/3 less than Kimmie, so she earned 2/3 of $450
    total_earnings = kimmie_earnings + zahra_earnings  # Calculate the total earnings of both Kimmie and Zahra

    savings_amount = (total_earnings / 2)  # Both Kimmie and Zahra save half of their earnings
    result = savings_amount
    return result

print(solution())