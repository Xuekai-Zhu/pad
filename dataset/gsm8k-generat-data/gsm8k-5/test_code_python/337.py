def solution():
    wine = 26  # Number of people who took wine
    soda = 22  # Number of people who took soda
    both = 17  # Number of people who took both wine and soda

    # Calculate the total number of people at the gathering
    total_people = wine + soda - both
    result = total_people
    return result

print(solution())