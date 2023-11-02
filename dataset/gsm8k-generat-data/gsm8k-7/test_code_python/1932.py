def solution():
    num_players = 60
    admission_fee = 40
    num_parties = 8

    # Calculate the total amount collected in all 8 parties
    total_collected = num_players * admission_fee * num_parties
    result = total_collected
    return result

print(solution())