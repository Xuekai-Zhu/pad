def solution():
    berries_per_bird_per_day = 7  # Each bird eats 7 berries a day
    num_birds = 5  # Samuel has 5 birds
    days = 4  # Samuel wants to know how many berries his birds will eat in 4 days

    # Calculate the total number of berries Samuel's birds will eat in 4 days
    total_berries = berries_per_bird_per_day * num_birds * days
    result = total_berries
    return result

print(solution())