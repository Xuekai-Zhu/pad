def solution():
    total_visitors = 500
    percent_ill = 40
    visitors_not_ill = total_visitors - (total_visitors * (percent_ill / 100))
    result = visitors_not_ill
    return result

print(solution())