def solution():
    charlemagne_father = "Pepin the Short"
    pepin_father = "Charles Martel"
    pepin_early_years = "raised by monks"
    battle_of_tours_leader = "Charles Martel"
    
    # Check if Charlemagne's father was instrumental in the outcome of the Battle of Tours
    if charlemagne_father == pepin_father and pepin_early_years == "raised by monks" and charlemagne_father != battle_of_tours_leader:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())