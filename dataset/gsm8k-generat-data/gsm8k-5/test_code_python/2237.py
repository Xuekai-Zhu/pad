def solution():
    birthday_money = 100  # Mary's brother surprised her with $100
    video_game_cost = birthday_money / 4  # Mary spent a quarter of her birthday money on a new video game
    remaining_money = birthday_money - video_game_cost  # Calculate the remaining money after buying the video game
    goggles_cost = remaining_money / 5  # Mary used a fifth of the remaining money on swimming goggles
    remaining_money -= goggles_cost  # Calculate the remaining money after buying the goggles
    result = remaining_money
    return result

print(solution())