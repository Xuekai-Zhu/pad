def solution():
     history_pages = 160
     geography_pages = history_pages + 70
     math_pages = (history_pages + geography_pages) / 2
     science_pages = history_pages * 2
     total_pages = history_pages + geography_pages + math_pages + science_pages
     
     return total_pages

print(solution())