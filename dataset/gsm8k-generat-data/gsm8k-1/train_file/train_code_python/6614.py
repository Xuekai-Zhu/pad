def solution():
 """Pete and Raymond each receive $2.50 from their grandmother. Pete saves his money and only spends 4 nickels. Raymond spends his money at the arcade games but still has 7 dimes left. How much did Pete and Raymond spent altogether, in cents?"""
 pete_money = 2.50
 pete_spent = 0.20    # 4 nickels = 0.20
 raymond_money = 2.50
 raymond_spent = (raymond_money - pete_spent) - 1.00    # arcade games cost $1.00 each
 total_spent = (pete_spent + raymond_spent) * 100    # converting to cents
 result = int(total_spent)    # casting to int for a whole number
        
 return result

print(solution())