def solution():
    num_fish_caught_per_day = 2
    num_days = 30
    num_fish_fillets_per_fish = 2

    # Calculate the total number of fish caught over the summer break
    total_fish_caught = num_fish_caught_per_day * num_days

    # Calculate the total number of fish fillets
    total_fish_fillets = total_fish_caught * num_fish_fillets_per_fish

    result = total_fish_fillets
    return result

print(solution())