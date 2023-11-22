def solution():
    
    # Define the number of sacks of rice and the number of sacks given away
    sacks_of_rice = 20
    sacks_given_away = 3 + 4

    # Calculate the total number of sacks of rice
    total_sacks = sacks_of_rice + sacks_given_away

    # Calculate the total amount of rice given away
    total_given_away = total_sacks * 25

    # return the result
    result = total_given_away
    return result

print(solution())