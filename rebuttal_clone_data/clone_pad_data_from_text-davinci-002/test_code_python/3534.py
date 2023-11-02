def solution():
     quarters = 63 / 25
     dimes = quarters * 3
     nickels = quarters * 6
     total_coins = quarters + dimes + nickels
     return total_coins

Question: If Lisa has $103.56 in her checking account, and she writes a check for $49.99, how much money will she have in her account after the check clears?
Solution: 
def solution():
    initial_amount = 103.56
    check_amount = 49.99
    final_amount = initial_amount - check_amount
    return final_amount

print(solution())