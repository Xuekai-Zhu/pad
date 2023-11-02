def solution():
     """Liza bought 10 kilograms of butter to make cookies. She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. How many kilograms of butter are left after making those three kinds of cookies?"""
     total_kilos = 10
     butter_used = total_kilos / 2 + total_kilos / 5 + (total_kilos - ((total_kilos / 2) + (total_kilos / 5))) / 3
     butter_left = total_kilos - butter_used
     result = butter_left
     return result

print(solution())