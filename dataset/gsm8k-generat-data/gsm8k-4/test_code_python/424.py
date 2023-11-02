def solution():
    """Rose had 10 kilograms of rice. She cooked 9/10 kilograms in the morning and 1/4 of the remaining in the evening. How many grams of rice did she have left?"""
    # Define the initial amount of rice
    rice = 10

    # Cook 9/10 kilograms in the morning
    rice -= 9/10

    # Calculate the remaining amount of rice in kilograms
    remaining_rice = rice

    # Cook 1/4 of the remaining amount in the evening
    remaining_rice -= remaining_rice/4

    # Convert the remaining amount of rice to grams
    remaining_rice *= 1000

    # return the result in grams
    result = remaining_rice
    return result

print(solution())