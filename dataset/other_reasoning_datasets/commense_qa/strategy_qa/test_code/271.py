def solution():
    japan_survival_rate = 0.847
    sweden_survival_rate = 0.862
    if japan_survival_rate > sweden_survival_rate:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())