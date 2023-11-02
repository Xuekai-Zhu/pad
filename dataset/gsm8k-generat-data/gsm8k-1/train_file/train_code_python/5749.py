def solution():
    """Vicente saw Sophie's mom giving Sophie 20 oranges every day to carry to school to eat. He also saw Hannah's dad giving Hannah 40 grapes every day to eat at the school. If he counted the number of fruits that the girls were given for 30 days, calculate the total number of fruits that Sophie and Hannah had eaten in the 30 days."""
    sophie_oranges_per_day = 20
    hannah_grapes_per_day = 40
    days = 30
    sophie_total_oranges = sophie_oranges_per_day * days
    hannah_total_grapes = hannah_grapes_per_day * days
    total_fruits_eaten = sophie_total_oranges + hannah_total_grapes
    result = total_fruits_eaten
    return result

print(solution())