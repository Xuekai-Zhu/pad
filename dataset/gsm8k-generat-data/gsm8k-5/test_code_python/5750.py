def solution():
    oranges_per_day = 20  # Sophie's mom gives her 20 oranges per day
    grapes_per_day = 40  # Hannah's dad gives her 40 grapes per day
    days = 30  # The girls were given fruits for 30 days

    # Calculate the total number of oranges Sophie ate in 30 days
    total_oranges = oranges_per_day * days

    # Calculate the total number of grapes Hannah ate in 30 days
    total_grapes = grapes_per_day * days

    # Calculate the total number of fruits the girls ate in 30 days
    total_fruits = total_oranges + total_grapes
    result = total_fruits
    return result

print(solution())