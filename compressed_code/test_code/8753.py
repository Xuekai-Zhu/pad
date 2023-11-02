def solution():
    
    lucca_total_balls = 100
    lucca_basketballs_percent = 10
    lucca_basketballs = lucca_total_balls * (lucca_basketballs_percent / 100)
    
    lucien_total_balls = 200
    lucien_basketballs_percent = 20
    lucien_basketballs = lucien_total_balls * (lucien_basketballs_percent / 100)
    
    total_basketballs = lucca_basketballs + lucien_basketballs
    result = total_basketballs
    
    return result

print(solution())