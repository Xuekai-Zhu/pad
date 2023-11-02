def solution():
     """Lee mows one lawn and charges $33. Last week he mowed 16 lawns and three customers each gave him a $10 tip. How many dollars did Lee earn mowing lawns last week?"""
     lawns_mowed = 16
     tips = 3 * 10
     income = lawns_mowed * 33 + tips
     result = income
    return result

print(solution())