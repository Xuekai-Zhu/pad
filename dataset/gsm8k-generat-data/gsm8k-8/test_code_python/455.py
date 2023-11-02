def solution():
    # Determine how many times the amoeba needs to divide to reach 16 amoebae
    division_count = 4 # Since 2^4 = 16

    # Calculate the number of days it will take for the amoeba to divide into 16 amoebae
    days_to_divide = division_count * 2

    result = days_to_divide
    return result

print(solution())