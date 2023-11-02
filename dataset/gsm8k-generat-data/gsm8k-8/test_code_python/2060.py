def solution():
    # Define the amount of milk provided by the cow
    milk_per_day = 16

    # Calculate the amount of milk consumed by Daisy's kids
    kids_milk = milk_per_day * 0.75

    # Calculate the amount of milk remaining after the kids have their share
    remaining_milk = milk_per_day - kids_milk

    # Calculate the amount of milk used for cooking
    cooking_milk = remaining_milk * 0.5

    # Calculate the amount of milk left over
    leftover_milk = remaining_milk - cooking_milk
    result = leftover_milk
    return result

print(solution())