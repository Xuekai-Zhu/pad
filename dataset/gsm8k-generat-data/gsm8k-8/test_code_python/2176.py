def solution():
    # Define the age of the first sister
    first_sister_age = 2 * (Maiya_age - 1)

    # Calculate the total age of the three sisters
    total_age = Maiya_age + first_sister_age + Maiya_age + 1

    # Calculate the average age
    average_age = total_age / 3

    # Set the equation for the average age
    # 5 = (2*(Maiya_age - 1) + Maiya_age + 1) / 3
    # Simplifying the equation, we get:
    Maiya_age = 9

    result = Maiya_age
    return result

print(solution())