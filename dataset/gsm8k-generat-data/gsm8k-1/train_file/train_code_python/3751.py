def solution():
    """Lucca has 100 balls and 10 percent of his balls are basketballs. Lucien has 200 balls and 20 percent of them are basketballs. In total how many basketballs do Lucca and Lucien have?"""
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