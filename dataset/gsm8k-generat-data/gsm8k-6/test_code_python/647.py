def solution():
    # Calculate the total number of cupcakes given away
    cupcakes_given_away = 18 + 16 + 4  # cupcakes given to Ms. Delmont's class, Mrs. Donnelly's class, Ms. Delmont, Mrs. Donnelly, nurse, and principal

    # Calculate the number of cupcakes left over
    cupcakes_left_over = 40 - cupcakes_given_away
    
    result = cupcakes_left_over
    return result

print(solution())