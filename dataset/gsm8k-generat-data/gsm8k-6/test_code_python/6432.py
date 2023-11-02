def solution():
    # Find half of Marco's money and subtract it from his initial amount
    marco_after_half = 24 - (1/2 * 24)
    
    # Add the amount Mary spends to her initial amount
    mary_after_spend = 15 - 5
    
    # Find the difference between Mary's amount after spending and Marco's amount after giving her half
    difference = mary_after_spend - marco_after_half
    
    result = difference
    return result

print(solution())