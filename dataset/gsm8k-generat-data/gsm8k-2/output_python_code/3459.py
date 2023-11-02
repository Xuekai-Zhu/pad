def solution():
   """Aaron and his brother Carson each saved up $40 to go to dinner. The bill is 3/4 of their total money. After, they go out for ice cream. Each scoop costs $1.5 and they get the same amount as each other. If they leave with $1 in change each, how many scoops did they each buy?"""
   dinner_bill = (3/4) * 80
   money_left = (2 * 40) - dinner_bill - 2
   num_scoops = money_left // 3
   result = num_scoops
   return result

print(solution())