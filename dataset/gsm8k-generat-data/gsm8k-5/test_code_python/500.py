def solution():
    catches_joe = 23  # Joe caught the ball 23 times
    catches_derek = 2*catches_joe - 4  # Derek caught four less than double the catches Joe did
    catches_tammy = (1/3)*catches_derek + 16  # Tammy caught sixteen more than a third of the times Derek did

    result = catches_tammy
    return result

print(solution())