def solution():
    # Using algebra, we can solve for the original amount of money that Jerome had
    # Let x be the original amount of money
    # We know that (1/2)x = 43, so x = 86

    original_money = 86
    
    # Jerome gave $8 to Meg
    money_after_meg = original_money - 8
    
    # Jerome gave thrice as much ($24) to Bianca
    money_after_bianca = money_after_meg - 24
    
    # Calculate how much money Jerome has left
    money_left = money_after_bianca
    
    result = money_left
    return result

print(solution())