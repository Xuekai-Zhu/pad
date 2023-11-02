def solution():
    # Define the number of Dodge vehicles on the lot
    dodge = 400 / 2

    # Define the number of Hyundai vehicles on the lot
    hyundai = dodge / 2

    # Define the number of Kia vehicles on the lot
    kia = 400 - (dodge + hyundai)

    result = kia
    return result

print(solution())