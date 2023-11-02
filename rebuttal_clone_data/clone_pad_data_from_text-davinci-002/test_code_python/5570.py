def solution():
     small_bonsai_cost = 30
     big_bonsai_cost = 20
     small_bonsai_sold = 3
     big_bonsai_sold = 5
     total_cost = (small_bonsai_cost * small_bonsai_sold) + (big_bonsai_cost * big_bonsai_sold)
     result = total_cost
     return result

Question: A recipe for candy calls for 3 parts sugar for every 2 parts chocolate.  How many parts sugar are needed for 18 parts chocolate?
Solution:
def solution():
    chocolate = 18
    sugar = chocolate * (3/2)
    result = sugar
    return result

print(solution())