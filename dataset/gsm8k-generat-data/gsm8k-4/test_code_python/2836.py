def solution():
    """During his summer break, Luke catches 2 fish every day for 30 days. If each fish gives him 2 fillets, then how many fish fillets does he have?"""
    # Define the number of days and the number of fish caught per day
    days = 30
    fish_per_day = 2

    # Calculate the total number of fish caught
    total_fish = days * fish_per_day

    # Calculate the total number of fish fillets
    fish_fillets = total_fish * 2

    # Return the result
    result = fish_fillets
    return result

print(solution())