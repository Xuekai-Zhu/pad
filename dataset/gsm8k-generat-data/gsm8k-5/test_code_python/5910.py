def solution():
    cups_before_zap = 5
    ounces_per_cup = 8
    total_ounces_before = cups_before_zap * ounces_per_cup  # Total ounces of coffee before zap

    # After using the shrink ray device, everything shrinks by 50%
    cups_after_zap = cups_before_zap / 2
    ounces_per_cup_after = ounces_per_cup / 2
    total_ounces_after = cups_after_zap * ounces_per_cup_after

    result = total_ounces_after
    return result

print(solution())