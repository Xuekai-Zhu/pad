def solution():
    fish_per_day = 2  # Luke catches 2 fish per day
    days = 30  # Luke catches fish for 30 days
    fillets_per_fish = 2  # Each fish gives 2 fillets

    # Calculate the total number of fish caught
    total_fish = fish_per_day * days

    # Calculate the total number of fillets
    total_fillets = total_fish * fillets_per_fish
    result = total_fillets
    return result

print(solution())