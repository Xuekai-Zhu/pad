def solution():
    # Calculate the number of catches Derek made
    catches_Derek = 2 * 23 - 4  # Derek made four less than double the catches Joe did
    # Calculate the number of catches Tammy made
    catches_Tammy = (1/3) * catches_Derek + 16  # Tammy caught the ball sixteen more than a third of the times Derek did
    result = catches_Tammy
    return result

print(solution())