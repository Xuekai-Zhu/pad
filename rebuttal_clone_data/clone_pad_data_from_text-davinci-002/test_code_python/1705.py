def solution():
     flowers_bought = 3
     flowers_free = 2
     total_flowers = (flowers_bought * 12) + flowers_free
     result = total_flowers
     return result
     
Question: Jennie spends 1/5 of her paycheck on rent, 1/10 on utilities, and the rest on groceries. Her rent is $600, and her utilities are $100. She spends the rest of her paycheck on groceries. How much money is left for groceries?
Solution:
def solution():
    total_percent = 1/5 + 1/10
    rent = 600
    utilities = 100
    remainder_percent = 1 - total_percent
    paycheck = rent + utilities
    groceries = remainder_percent * paycheck
    result = groceries
    
    return result

print(solution())