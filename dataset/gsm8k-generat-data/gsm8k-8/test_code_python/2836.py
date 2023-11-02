def solution():
    # Define the number of fish caught each day and the number of days
    fish_per_day = 2
    days = 30

    # Calculate the total number of fish caught
    total_fish = fish_per_day * days

    # Calculate the total number of fillets
    total_fillets = total_fish * 2

    result = total_fillets
    return result

print(solution())