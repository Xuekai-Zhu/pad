def solution():
    
    # Define the initial number of riders and the percentage of surfers that can stay upright
    initial_riders = 100
    stay_upright_percentage = 0.25

    # Calculate the number of surfers that can stay upright
    stay_upright_riders = initial_riders * stay_upright_percentage

    # Calculate the number of women
    women = riders * 0.6

    # Calculate the number of men that can stay upright
    men_stay_upright = stay_upright_riders - women

    # Display the number of men that can stay upright
    result = men_stay_upright
    return result

print(solution())