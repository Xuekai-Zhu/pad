def solution():
     diaries = 8
     diaries_bought = diaries * 2
     diaries_lost = diaries_bought / 4
     diaries_now = diaries_bought - diaries_lost
     result = diaries_now
     return result

print(solution())