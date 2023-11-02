def solution():
     papers_delivered_daily = 100
     papers_delivered_weekly = papers_delivered_daily * 6
     papers_delivered_on_sunday = 30
     total_papers_delivered = papers_delivered_weekly + papers_delivered_on_sunday
     result = total_papers_delivered
     return result

print(solution())