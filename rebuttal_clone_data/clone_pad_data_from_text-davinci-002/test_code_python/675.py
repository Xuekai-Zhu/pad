def solution():
    lawsuit_1_wins = 0.3
    lawsuit_1_losses = 0.7
    lawsuit_2_wins = 0.5
    lawsuit_2_losses = 0.5
    both_suits_won = lawsuit_1_wins * lawsuit_2_wins
    both_suits_lost = lawsuit_1_losses * lawsuit_2_losses
    percent_chance_both_suits_won = both_suits_won * 100
    percent_chance_both_suits_lost = both_suits_lost * 100
    result = percent_chance_both_suits_lost - percent_chance_both_suits_won
    
    return result

print(solution())