def solution():
    # Define the number of toys Anais has more than Kamari
    anais_extra = 30

    # Define the total number of toys
    total_toys = 160

    # Calculate Kamari's number of toys
    kamari_toys = (total_toys - anais_extra) / 2

    result = kamari_toys
    return result

print(solution())