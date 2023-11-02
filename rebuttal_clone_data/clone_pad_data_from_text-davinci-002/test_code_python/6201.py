def solution():
     total_comics = 300
     comics_liked_by_females = total_comics * 0.30
     comics_liked_by_males = total_comics * 0.40
     comics_liked_by_both = total_comics * 0.30
     comics_disliked_by_both = total_comics - comics_liked_by_females - comics_liked_by_males - comics_liked_by_both
     comics_disliked_by_both_percent = comics_disliked_by_both / total_comics
     result = comics_disliked_by_both_percent
     return result

print(solution())