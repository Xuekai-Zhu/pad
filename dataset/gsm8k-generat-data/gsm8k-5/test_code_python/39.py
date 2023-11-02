def solution():
    candy_per_house_anna = 14  # Anna gets 14 pieces of candy per house
    candy_per_house_billy = 11  # Billy gets 11 pieces of candy per house
    num_houses_anna = 60  # Anna goes to 60 houses
    num_houses_billy = 75  # Billy goes to 75 houses

    # Calculate the total number of candies Anna and Billy get
    total_candy_anna = candy_per_house_anna * num_houses_anna
    total_candy_billy = candy_per_house_billy * num_houses_billy

    # Calculate the difference in the number of candies Anna and Billy get
    diff_candy = total_candy_anna - total_candy_billy
    result = diff_candy
    return result

print(solution())