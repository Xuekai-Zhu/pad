def solution():
    """During his summer break, Luke catches 2 fish every day for 30 days. If each fish gives him 2 fillets, then how many fish fillets does he have?"""
    fish_per_day = 2
    total_days = 30
    fillets_per_fish = 2
    total_fish = fish_per_day * total_days
    total_fillets = total_fish * fillets_per_fish
    result = total_fillets
    return result

print(solution())