def solution():
    # Define the characteristics of Mixed Martial Arts in the UFC and Roman Colosseum games
    mma_enclosed_structure = "The Octagon"
    colosseum_enclosed_arenas = True
    mma_contest_stopped_when_incapacitated = True
    colosseum_fought_until_last_man_standing = True
    mma_crowd_size = 56000
    colosseum_crowd_size = "in the tens of thousands"

    # Check if Mixed Martial Arts in the UFC is totally original from Roman Colosseum games
    if mma_enclosed_structure != "" and mma_contest_stopped_when_incapacitated and mma_crowd_size > colosseum_crowd_size:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())