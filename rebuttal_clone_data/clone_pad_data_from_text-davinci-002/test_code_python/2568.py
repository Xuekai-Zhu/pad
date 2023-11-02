def solution():
     eggs_with_double_yolks = 5
     yolks_in_double_yolked_eggs = 2
     yolks_in_regular_eggs = 1
     total_yolks = (eggs_with_double_yolks * yolks_in_double_yolked_eggs) + ((12 - eggs_with_double_yolks) * yolks_in_regular_eggs)
     result = total_yolks
     return result

print(solution())