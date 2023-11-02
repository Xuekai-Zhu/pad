def solution():
    nose_price = 20
    ears_price = nose_price * 1.5
    num_noses = 6
    num_ears = 9

    # Calculate the total earnings from nose piercings
    nose_earnings = num_noses * nose_price

    # Calculate the total earnings from ear piercings
    ears_earnings = num_ears * ears_price

    # Calculate the total earnings from all piercings
    total_earnings = nose_earnings + ears_earnings
    result = total_earnings
    return result

print(solution())