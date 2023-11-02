def solution():
     total_kids = 16 + 14
     boys_who_brought_gifts = 16 * (3/4)
     girls_who_brought_gifts = 14 * (6/7)
     kids_who_brought_gifts = boys_who_brought_gifts + girls_who_brought_gifts
     kids_who_didnt_bring_gifts = total_kids - kids_who_brought_gifts
     result = kids_who_didnt_bring_gifts
     return result

print(solution())