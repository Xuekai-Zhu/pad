def solution():
     sneakers_cost = 90
     money_saved = 15
     money_needed = sneakers_cost - money_saved
     action_figures_sold = 10
     money_leftover = 25
     money_earned = money_needed + money_leftover
     price_per_action_figure = money_earned / action_figures_sold
     result = price_per_action_figure
     return result

print(solution())