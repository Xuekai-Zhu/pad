def solution():
    """Gunther, the gorilla, had 48 bananas hidden under a fern branch. When Gunther wasn't looking, Arnold, the chimpanzee, stole half of the bananas from the pile. The next day, Gunther added another 25 bananas to his pile, but later that evening, Arnold stole another 12 of the bananas. On the third day, Gunther added another 6 bananas to his pile and began counting bananas. How many bananas did Gunther find were in the pile?"""
    bananas_start = 48
    bananas_stolen_day1 = bananas_start / 2
    bananas_after_day1 = bananas_start - bananas_stolen_day1 + 25
    bananas_stolen_day2 = 12
    bananas_after_day2 = bananas_after_day1 - bananas_stolen_day2 + 6
    result = bananas_after_day2
    return result

print(solution())