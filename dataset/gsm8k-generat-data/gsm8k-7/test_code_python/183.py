def solution():
    initial_chickens = 300
    initial_turkeys = 200
    initial_guinea_fowls = 80
    chicken_loss_per_day = 20
    turkey_loss_per_day = 8
    guinea_fowl_loss_per_day = 5
    days = 7

    # Calculate the remaining number of chickens after a week
    remaining_chickens = initial_chickens - (chicken_loss_per_day * days)

    # Calculate the remaining number of turkeys after a week
    remaining_turkeys = initial_turkeys - (turkey_loss_per_day * days)

    # Calculate the remaining number of guinea fowls after a week
    remaining_guinea_fowls = initial_guinea_fowls - (guinea_fowl_loss_per_day * days)

    # Calculate the total number of birds remaining after a week
    total_birds_remaining = remaining_chickens + remaining_turkeys + remaining_guinea_fowls
    result = total_birds_remaining
    return result

print(solution())