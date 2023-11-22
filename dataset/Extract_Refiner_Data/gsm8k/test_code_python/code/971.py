def solution():
    
    total_cherries = 60
    robert_cherries = 30
    richard_cherries = robert_cherries + 10
    jerry_cherries = total_cherries - robert_cherries - richard_cherries
    difference = robert_cherries - jerry_cherries
    result = difference
    return result

print(solution())