def solution():
    """Marco has $24. Mary has $15. If Marco gives Mary half of what he has, Mary will have more than Marco. But Mary spends $5. How much more money does Mary have than Marco?"""
    
    # Define Marco's and Mary's initial amounts
    marco_money = 24
    mary_money = 15
    
    # Marco gives Mary half of what he has
    marco_money = marco_money / 2
    mary_money += marco_money
    
    # Mary spends $5
    mary_money -= 5
    
    # Calculate the difference in money between Mary and Marco
    difference = mary_money - marco_money
    
    # Display the result
    result = difference
    return result

print(solution())