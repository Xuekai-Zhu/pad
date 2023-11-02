def solution():
     """Pam has some bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. Gerald's bags have 40 apples each. If Pam has 1200 apples in total, how many bags of apples does she have?"""
     pam_apples = 1200
     gerald_apples = 40
     pam_bags = pam_apples / (gerald_apples * 3)
     result = pam_bags
     return result

print(solution())