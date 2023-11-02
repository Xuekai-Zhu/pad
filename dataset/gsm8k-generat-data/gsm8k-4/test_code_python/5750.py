def solution():
    """Vicente saw Sophie's mom giving Sophie 20 oranges every day to carry to school to eat. He also saw Hannah's dad giving Hannah 40 grapes every day to eat at the school. If he counted the number of fruits that the girls were given for 30 days, calculate the total number of fruits that Sophie and Hannah had eaten in the 30 days."""
    
    # Define the number of fruits given to each girl every day
    sophie_oranges = 20
    hannah_grapes = 40

    # Calculate the total number of fruits given to each girl in 30 days
    sophie_total = sophie_oranges * 30
    hannah_total = hannah_grapes * 30

    # Calculate the total number of fruits eaten by both girls in 30 days
    total_fruits = sophie_total + hannah_total

    # return the result
    result = total_fruits
    return result

print(solution())