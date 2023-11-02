def solution():
    
    johnson_share = 5
    mike_share = 2
    johnson_amount = 2500
    total_share = johnson_share + mike_share
    mike_amount = (mike_share / total_share) * (johnson_amount / (johnson_share / total_share))
    mike_amount -= 200  
    result = round(mike_amount, 2)
    return result

print(solution())