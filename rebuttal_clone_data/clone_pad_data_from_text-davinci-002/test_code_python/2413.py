def solution():
     nickels_before = 20
     dimes = 3 * nickels_before
     nickels_accidentally_found = 2 * nickels_before
     total_nickels = nickels_before + nickels_accidentally_found
     total_dimes = dimes + (nickels_accidentally_found / 2)
     total_value = (total_dimes * 10) + (total_nickels * 5)
     result = total_value
     return result

print(solution())