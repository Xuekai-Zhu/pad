def solution():
    # Initial counts of each type of bird
    chickens = 300
    turkeys = 200
    guinea_fowls = 80

    # Daily losses of each type of bird
    chicken_loss = 20
    turkey_loss = 8
    guinea_fowl_loss = 5

    # Calculate the total losses in a week
    total_loss = (chicken_loss + turkey_loss + guinea_fowl_loss) * 7

    # Calculate the remaining counts of each type of bird
    remaining_chickens = chickens - (chicken_loss * 7)
    remaining_turkeys = turkeys - (turkey_loss * 7)
    remaining_guinea_fowls = guinea_fowls - (guinea_fowl_loss * 7)

    # Calculate the total remaining birds
    total_remaining_birds = remaining_chickens + remaining_turkeys + remaining_guinea_fowls
    result = total_remaining_birds
    return result

print(solution())