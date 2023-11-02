def solution():
    # Calculate the total money earned from nose piercings
    nose_money = 20 * 6  # Jerry charges $20 for each nose piercing and he did 6 of them

    # Calculate the total money earned from ear piercings
    ear_money = 1.5 * 20 * 9  # Jerry charges 50% more for ear piercings, so he charges $30 for each ear piercing and he did 9 of them

    # Calculate the total money Jerry made
    total_money = nose_money + ear_money
    result = total_money
    return result

print(solution())