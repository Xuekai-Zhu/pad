def solution():
    total_vodka = 8  # Jake splits 8 shots of vodka with his friend
    amount_per_shot = 1.5  # Each shot of vodka is 1.5 ounces
    purity = 0.5  # The vodka is 50% pure alcohol

    # Calculate the total amount of pure alcohol consumed by Jake
    total_alcohol = total_vodka * amount_per_shot * purity

    result = total_alcohol
    return result

print(solution())