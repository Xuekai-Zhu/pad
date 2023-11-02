def solution():
    # Calculate the total amount earned by Brady
    card_pay = 0.7  # amount earned per card
    bonus = 0  # initialize bonus to 0
    
    if (200 >= 100):  # check if Brady transcribed more than 100 cards
        bonus += 10 * (200 // 100)  # add bonus for every 100 cards transcribed
        
    total_earnings = (card_pay * 200) + bonus  # total earnings for 200 cards
    
    result = total_earnings
    return result

print(solution())