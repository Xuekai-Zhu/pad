def solution():
    total_minnows = 600  # Jane bought 600 minnows
    num_people_playing = 800  # 800 people are playing the game
    chance_of_winning = 0.15  # 15% of players will win a prize
    num_prizes = num_people_playing * chance_of_winning  # Calculate the number of prizes that will be given out
    num_minnows_used = num_prizes * 3  # Each prize consists of 3 minnows
    num_minnows_left = total_minnows - num_minnows_used  # Calculate the number of minnows left over
    result = num_minnows_left
    return result

print(solution())