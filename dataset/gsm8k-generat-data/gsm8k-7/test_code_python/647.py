def solution():
    total_cupcakes = 40
    delmont_class = 18
    donnelly_class = 16
    extra_people = 4 # Ms. Delmont, Mrs. Donnelly, nurse, principal

    # Calculate the total number of cupcakes given away
    given_away = (delmont_class + donnelly_class + extra_people)

    # Calculate the number of cupcakes left over
    left_over = total_cupcakes - given_away
    result = left_over
    return result

print(solution())