def solution():
    guests = 10  # Alex invited 10 friends over
    non_meat_eater = 1  # 1 friend doesn't eat meat
    no_buns = 1  # 1 friend doesn't eat buns
    burgers_per_guest = 3  # Alex planned to cook 3 burgers for each guest
    buns_per_pack = 8  # There are 8 buns in each pack

    # Calculate the number of burgers needed
    total_burgers = guests * burgers_per_guest  # Alex needs to cook burgers for all his guests
    total_burgers -= non_meat_eater  # Subtract the non-meat eater
    total_buns = total_burgers * 2  # Each burger needs 2 buns

    # Calculate the number of buns packs needed
    packs_of_buns = total_buns // buns_per_pack + (total_buns % buns_per_pack > 0)  # Round up to the nearest whole pack

    result = packs_of_buns
    return result

print(solution())