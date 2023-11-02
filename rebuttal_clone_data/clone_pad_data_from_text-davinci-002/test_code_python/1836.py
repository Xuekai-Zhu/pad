def solution():
     candies_to_start = 6 + 11 + 9
     candies_after_father_buys_more = 8 + 11 + (36 - 8 - 11)
     candies_left_for_andy = candies_after_father_buys_more - 8 - 11
     candies_more_than_caleb = candies_left_for_andy - 6
     result = candies_more_than_caleb
     return result

print(solution())