def solution():
     price_per_lawn = 15
     video_game_cost = 45
     book_cost = 5
     number_of_lawns_mowed = 35
     video_games_purchased = 5
     money_made = number_of_lawns_mowed * price_per_lawn
     money_spent = (video_game_cost * video_games_purchased) + book_cost
     money_leftover = money_made - money_spent
     books_purchased = money_leftover / book_cost
     result = books_purchased
 
     return result

print(solution())