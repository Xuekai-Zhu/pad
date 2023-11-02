def solution():
    nba_average_height = 79 # 6ft 7in = 79in
    mussolini_height = 66.5 # 5ft 6.5in = 66.5in
    if mussolini_height >= nba_average_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())