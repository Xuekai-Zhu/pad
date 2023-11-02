def solution():
    num_guests = 10
    burgers_per_guest = 3
    non-meat_eater = 1
    non-bread_eater = 1
    buns_per_pack = 8

    # Calculate the total number of burgers needed
    total_burgers = num_guests * burgers_per_guest

    # Subtract the burger for the non-meat eater
    total_burgers -= burgers_per_guest

    # Calculate the total number of buns needed
    total_buns = total_burgers

    # Subtract the buns not needed by the non-bread eater
    total_buns -= burgers_per_guest

    # Calculate the number of packs of buns needed
    num_bun_packs = total_buns // buns_per_pack + 1 if total_buns % buns_per_pack != 0 else total_buns // buns_per_pack
    result = num_bun_packs
    return result

print(solution())