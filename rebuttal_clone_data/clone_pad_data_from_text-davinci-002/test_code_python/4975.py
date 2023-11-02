def solution():
     total_figures = 24
     sold_figures = total_figures / 4
     given_away = (total_figures - sold_figures) / 3
     left_over = total_figures - sold_figures - given_away
     result = left_over
     return result

print(solution())