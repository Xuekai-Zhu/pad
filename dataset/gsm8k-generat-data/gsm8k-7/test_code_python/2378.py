def solution():
    lego_set_price = 250
    num_lego_sets = 3

    toy_sword_price = 120
    num_toy_swords = 7

    play_dough_price = 35
    num_play_doughs = 10

    # Calculate the total cost of all lego sets
    total_lego_sets_cost = lego_set_price * num_lego_sets

    # Calculate the total cost of all toy swords
    total_toy_swords_cost = toy_sword_price * num_toy_swords

    # Calculate the total cost of all play doughs
    total_play_doughs_cost = play_dough_price * num_play_doughs

    # Calculate the total cost of all items
    total_cost = total_lego_sets_cost + total_toy_swords_cost + total_play_doughs_cost
    result = total_cost
    return result

print(solution())