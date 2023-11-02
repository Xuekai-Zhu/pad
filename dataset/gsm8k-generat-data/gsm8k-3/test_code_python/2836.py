def solution():
    """During his summer break, Luke catches 2 fish every day for 30 days.  If each fish gives him 2 fillets, then how many fish fillets does he have?"""
    # Define the number of fish caught per day and the number of days
    fish_per_day = 2
    days = 30

    # Calculate the total number of fish caught
    total_fish = fish_per_day * days

    # Calculate the total number of fillets
    total_fillets = total_fish * 2

    # Display the total number of fillets
    result = total_fillets
    return result

print(solution())