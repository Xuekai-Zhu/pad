def solution():
   Pennies = 200
    old_pennies = 30
    new_pennies = Pennies - old_pennies
    pennies_thrown_out = new_pennies * 0.2
    pennies_left = new_pennies - pennies_thrown_out
    result = pennies_left
    return result

print(solution())