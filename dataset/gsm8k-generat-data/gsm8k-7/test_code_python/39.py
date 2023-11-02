def solution():
    candy_per_house_anna = 14
    candy_per_house_billy = 11
    num_houses_anna = 60
    num_houses_billy = 75

    # Calculate the total number of candy pieces Anna gets
    total_candy_anna = candy_per_house_anna * num_houses_anna

    # Calculate the total number of candy pieces Billy gets
    total_candy_billy = candy_per_house_billy * num_houses_billy

    # Calculate the difference in candy pieces between Anna and Billy
    candy_difference = total_candy_anna - total_candy_billy
    result = candy_difference
    return result

print(solution())