def solution():
    small_cargo_weight = 5
    small_cargo_price = 2.5
    large_cargo_weight = 8
    large_cargo_price = 4
    num_small_cargoes_per_day = 4
    num_large_cargoes_per_day = 2
    num_days_per_week = 7

    # Calculate the total earnings from small cargoes per day
    total_small_earnings_per_day = num_small_cargoes_per_day * small_cargo_price

    # Calculate the total earnings from large cargoes per day
    total_large_earnings_per_day = num_large_cargoes_per_day * large_cargo_price

    # Calculate the total earnings per day
    total_earnings_per_day = total_small_earnings_per_day + total_large_earnings_per_day

    # Calculate the total earnings per week
    total_earnings_per_week = total_earnings_per_day * num_days_per_week
    result = total_earnings_per_week
    return result

print(solution())