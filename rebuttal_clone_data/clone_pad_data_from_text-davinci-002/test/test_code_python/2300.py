def solution():
     clowns = 4
     children = 30
     candies = 700
     sold_candies = 20
     remaining_candies = candies - (sold_candies * (clowns+children))
     result = remaining_candies
     return result

print(solution())