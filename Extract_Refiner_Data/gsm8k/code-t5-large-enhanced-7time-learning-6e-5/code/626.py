def solution():
    
    # Define the total number of riders
    total_riders = 100

    # Calculate the number of riders who can stay upright
    upright_riders = total_riders * 0.25

    # Calculate the number of women
    women = total_riders * 0.6

    # Calculate the number of men who can stay upright
    upright_men = upright_riders - women

    # return the result
    result = upright_men
    return result

print(solution())