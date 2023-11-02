def solution():
    diana_rate = 4
    diana_total = 40
    
    hani_rate = diana_rate + 3
    
    hani_total = hani_rate * (diana_total // diana_rate)
    
    total_together = diana_total + hani_total
    
    result = total_together
    return result

print(solution())