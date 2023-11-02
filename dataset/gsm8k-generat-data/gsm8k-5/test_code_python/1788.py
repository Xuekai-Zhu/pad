def solution():
    lychees_in_carton = 500
    lychees_sold = lychees_in_carton / 2 # Mr. Shaefer sold half of the lychees
    lychees_at_home = lychees_in_carton - lychees_sold # Mr. Shaefer took home the remaining lychees
    lychees_eaten = lychees_at_home * (3/5) # 3/5 of the lychees were eaten
    lychees_remaining = lychees_at_home - lychees_eaten # Calculate the number of lychees remaining

    result = lychees_remaining
    return result

print(solution())