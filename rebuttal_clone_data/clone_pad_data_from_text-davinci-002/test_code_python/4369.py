def solution():
     discount = 10
     price = 10
     discount_amount = price * (discount / 100)
     total_price = price - discount_amount
     result = total_price
     return result


Question: Emma earned $10 on Monday by doing chores for her mom. On Tuesday and Wednesday, she earned $7 and $6 by doing chores for her neighbor. Based on this information, how much money did Emma earn in total this week?

Solution:
def solution():
    monday_earnings = 10
    tuesday_earnings = 7
    wednesday_earnings = 6
    total_earnings = monday_earnings + tuesday_earnings + wednesday_earnings
    result = total_earnings
    return result

print(solution())