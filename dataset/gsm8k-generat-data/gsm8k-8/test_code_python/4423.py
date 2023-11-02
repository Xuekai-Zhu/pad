def solution():
    # Define the total amount of money they have
    total_money = 15 + 12

    # Calculate how many bottles of soda they can buy
    soda_cost = 3
    soda_count = int((total_money - 15) / soda_cost)

    # Calculate how many servings of soda they have in total
    soda_servings = soda_count * 12

    # Calculate the number of servings per guest
    servings_per_guest = soda_servings / 8

    result = servings_per_guest
    return result

print(solution())