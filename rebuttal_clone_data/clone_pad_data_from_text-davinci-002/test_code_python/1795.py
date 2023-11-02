def solution():
    mary_friends_red_marbles = 2*30
    anie_friends_red_marbles = 2*mary_friends_red_marbles + 20
    jenny_friends_red_marbles = 30

    anie_friends_blue_marbles = 2*25
    jenny_friends_blue_marbles = 25

    mary_friends_blue_marbles = 0.5*anie_friends_blue_marbles

    total_red_marbles = mary_friends_red_marbles + anie_friends_red_marbles + jenny_friends_red_marbles
    total_blue_marbles = mary_friends_blue_marbles + anie_friends_blue_marbles + jenny_friends_blue_marbles

    return [total_red_marbles, total_blue_marbles]

print(solution())