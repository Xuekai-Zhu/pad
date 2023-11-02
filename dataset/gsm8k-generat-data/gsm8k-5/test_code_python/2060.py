def solution():
    milk_per_day = 16  # Daisy's cow provides 16 cups of milk per day
    kids_consumption = 0.75  # 75% of the milk is consumed by Daisy's kids
    daisy_consumption = 0.5  # 50% of the remaining milk is used by Daisy for cooking

    # Calculate the amount of milk consumed by Daisy's kids
    kids_milk = milk_per_day * kids_consumption

    # Calculate the remaining milk after Daisy's kids consume their portion
    remaining_milk = milk_per_day - kids_milk

    # Calculate the amount of milk Daisy uses for cooking
    daisy_milk = remaining_milk * daisy_consumption

    # Calculate the final amount of milk left over
    left_over_milk = remaining_milk - daisy_milk
    result = left_over_milk
    return result

print(solution())