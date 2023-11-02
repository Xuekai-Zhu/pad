def solution():
    total_apples = 60  # Yanna bought 60 apples
    apples_given_to_Zenny = 18  # Yanna gave 18 apples to Zenny
    apples_given_to_Andrea = 6  # Yanna gave 6 more apples to Andrea

    # Calculate the total number of apples given away
    total_given_away = apples_given_to_Zenny + apples_given_to_Andrea

    # Calculate the number of apples Yanna kept
    apples_kept = total_apples - total_given_away
    result = apples_kept
    return result

print(solution())