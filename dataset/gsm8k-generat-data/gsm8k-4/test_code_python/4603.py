def solution():
    """Matt has six cats and half of them are female. If each female cat has 7 kittens, and Matt sells 9 of them, what percentage of his remaining cats are kittens (rounded to the nearest percent)?"""
    # Define the total number of cats and the number of female cats
    total_cats = 6
    female_cats = total_cats / 2

    # Calculate the total number of kittens
    total_kittens = female_cats * 7

    # Calculate the number of remaining cats after selling 9 kittens
    remaining_cats = total_cats + total_kittens - 9

    # Calculate the percentage of remaining cats that are kittens
    kitten_percentage = (total_kittens / remaining_cats) * 100

    # Round the percentage to the nearest whole number
    rounded_percentage = round(kitten_percentage)

    # Return the result
    result = rounded_percentage
    return result

print(solution())