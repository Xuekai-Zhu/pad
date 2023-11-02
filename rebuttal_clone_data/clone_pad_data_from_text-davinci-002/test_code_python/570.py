def solution():
     num_dimes = 5
     val_dimes = 10
     num_quarters = 3
     val_quarters = 25
     num_nickels = 8
     val_nickels = 5
     num_pennies = 60
     val_pennies = 1
     
     total = num_dimes * val_dimes + num_quarters * val_quarters + num_nickels * val_nickels + num_pennies * val_pennies
     result = total
     return result

print(solution())