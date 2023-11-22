def solution():
    
    # Define the number of chimichangas made on Tuesdays, Wednesday and Friday
    tuesday_chimichangas = 125
    wednesday_chimichangas = 125
    friday_chimichangas = 2 * wednesday_chimichangas

    # Calculate the total number of chimichangas made on the three days
    total_chimichangas = tuesday_chimichangas + wednesday_chimichangas + friday_chimichangas

    # Display the total number of chimichangas made
    result = total_chimichangas
    return result

print(solution())