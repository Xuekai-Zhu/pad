def solution():
    # Calculate the total number of t-shirts Dan makes in 2 hours
    tshirts_hour1 = 60 / 12  # t-shirts made in first hour
    tshirts_hour2 = 60 / 6  # t-shirts made in second hour
    total_tshirts = tshirts_hour1 + tshirts_hour2  # total t-shirts made in 2 hours
    result = total_tshirts
    return result

print(solution())