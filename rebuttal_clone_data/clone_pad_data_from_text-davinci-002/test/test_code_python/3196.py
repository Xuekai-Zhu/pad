def solution():
    visitors_october = 100
    visitors_november = visitors_october + (visitors_october * 0.15)
    visitors_december = visitors_november + 15
    total_visitors = visitors_october + visitors_november + visitors_december
    result = total_visitors
    return result

print(solution())