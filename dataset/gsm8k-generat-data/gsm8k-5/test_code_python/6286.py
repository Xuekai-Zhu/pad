def solution():
    queen_starting_count = 12500  # The queen starts with 12500 bees
    daily_hatch_count = 3000 # 3000 bees hatch from the eggs every day
    daily_loss_count = 900 # The queen loses 900 bees every day
    days = 7 # The queen wants to know the total number of bees after 7 days

    # Calculate the total number of bees at the end of 7 days
    total_count = queen_starting_count + (daily_hatch_count - daily_loss_count) * days
    result = total_count
    return result

print(solution())