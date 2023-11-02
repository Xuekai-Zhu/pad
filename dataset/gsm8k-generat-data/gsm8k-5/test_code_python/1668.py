def solution():
    rock_weight = 1.5  # The average weight of a rock is 1.5 pounds
    sale_price = 4  # Jim gets $4 for every pound of rocks
    total_sale = 60  # Jim makes $60 off the sale

    # Calculate the total weight of rocks sold
    total_weight = total_sale / sale_price

    # Calculate the number of rocks based on the average weight of a rock
    num_rocks = total_weight / rock_weight
    result = num_rocks
    return result

print(solution())