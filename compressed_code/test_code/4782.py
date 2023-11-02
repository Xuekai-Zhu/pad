def solution():
    
    mp3_player_price = 120
    cd_price = 19
    savings = 55
    father_contribution = 20
    total_cost = mp3_player_price + cd_price
    total_contribution = savings + father_contribution
    remaining_cost = total_cost - total_contribution
    result = remaining_cost
    return result

print(solution())