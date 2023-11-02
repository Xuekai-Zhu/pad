def solution():
    starting_amount = 20  # Daria starts with $20 in her piggy bank
    weekly_amount = 10  # Daria adds $10 to her piggy bank each week
    vacuum_cleaner_cost = 120  # The vacuum cleaner costs $120

    # Calculate how much Daria needs to save
    amount_to_save = vacuum_cleaner_cost - starting_amount

    # Calculate how many weeks it will take Daria to save enough money
    weeks_to_save = amount_to_save / weekly_amount
    result = weeks_to_save
    return result

print(solution())