def solution():
     """Daniel has a collection of 346 video games. 80 of them, Daniel bought for $12 each. Of the rest, 50% were bought for $7. All others had a price of $3 each. How much did Daniel spend on all the games in his collection?"""
     games_bought_for_12 = 80
     games_bought_for_7 = 173
     games_bought_for_3 = 93
     total_cost = (games_bought_for_12 * 12) + (games_bought_for_7 * 7) + (games_bought_for_3 * 3)
     result = total_cost
     return result

print(solution())