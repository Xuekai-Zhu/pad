def solution():
    # Calculate the total earnings from nose piercings
    nose_earnings = 6 * 20

    # Calculate the 50% increase for ear piercings
    ear_increase = 0.5 * 20

    # Calculate the earnings from ear piercings
    ear_earnings = 9 * (20 + ear_increase)

    # Calculate the total earnings
    total_earnings = nose_earnings + ear_earnings
    result = total_earnings
    return result

print(solution())