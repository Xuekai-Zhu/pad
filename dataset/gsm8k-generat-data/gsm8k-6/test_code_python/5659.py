def solution():
    # Find the number of visitors in November and December
    visitors_november = 100 + (100 * 0.15)  # 15% increase in visitors from October
    visitors_december = visitors_november + 15  # 15 more visitors than in November

    # Find the total number of visitors for these three months
    total_visitors = 100 + visitors_november + visitors_december
    result = total_visitors
    return result

print(solution())