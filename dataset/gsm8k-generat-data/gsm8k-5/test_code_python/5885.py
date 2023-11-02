def solution():
    # Calculate the number of t-shirts Dan makes in the first hour
    tshirts_per_min_first_hour = 1 / 12  # Dan makes 1 t-shirt every 12 minutes
    tshirts_first_hour = tshirts_per_min_first_hour * 60  # Convert to t-shirts per hour

    # Calculate the number of t-shirts Dan makes in the second hour
    tshirts_per_min_second_hour = 1 / 6  # Dan makes 1 t-shirt every 6 minutes
    tshirts_second_hour = tshirts_per_min_second_hour * 60  # Convert to t-shirts per hour

    # Calculate the total number of t-shirts Dan makes in two hours
    total_tshirts = tshirts_first_hour + tshirts_second_hour
    result = total_tshirts
    return result

print(solution())