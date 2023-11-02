def solution():
    milk = 20
    eggs = 60
    flour = 25
    
    total = milk + eggs + flour
    
    fresh_milk = milk / total
    fresh_eggs = eggs / total
    fresh_flour = flour / total
    
    odds_all_three_good = fresh_milk * fresh_eggs * fresh_flour
    
    result = odds_all_three_good
    
    return result

print(solution())