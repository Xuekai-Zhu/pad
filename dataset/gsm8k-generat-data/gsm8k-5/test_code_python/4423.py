def solution():
    # Calculate total amount of money they have for party after buying the cake
    total_money = 15 + 12 - 15  # Monica brings $15, Michelle brings $12, cake costs $15

    # Calculate number of bottles of soda they can buy
    bottles_of_soda = total_money // 3  # Each bottle of soda costs $3

    # Calculate total number of soda servings
    total_servings = bottles_of_soda * 12  # Each bottle of soda has 12 servings

    # Calculate number of soda servings for each guest
    servings_per_guest = total_servings // 8  # There are 8 guests in total

    result = servings_per_guest
    return result

print(solution())