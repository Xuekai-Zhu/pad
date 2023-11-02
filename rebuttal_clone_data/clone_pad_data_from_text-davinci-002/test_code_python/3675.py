def solution():
     weeks = 2
     fee = 5
     total_fee = 0
     
     for i in range(weeks):
         total_fee += fee
         fee = fee * 2
    return total_fee
     
Question: Jennie has 50 mL of a 40% solution of acid.  She needs to create a 60% solution.  How much water does she need to add?
Solution:
def solution():
    initial_acid = 50
    initial_percent = 40
    desired_percent = 60
    desired_acid = initial_acid * (desired_percent / initial_percent)
    water_needed = desired_acid - initial_acid
    result = water_needed
    return result

print(solution())