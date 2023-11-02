def solution():
    # Calculate the total amount of cheese bought by Miley
    total_weight = (5 * 200) + 600 + ((2/3) * 5 * 200)  # 5 packs of swiss cheese (5 * 200), 600 grams of blue cheese, and one-third less white cheese (2/3) * 5 packs of white cheese (5 * 200)

    # Calculate the total cost of cheese bought by Miley
    total_cost = (5 * 6) + (total_weight/200) * 5 + (total_weight/200) * 8  # 5 packs of swiss cheese cost $6 each, white cheese cost $5, blue cheese cost $8
    result = total_cost
    return result

print(solution())