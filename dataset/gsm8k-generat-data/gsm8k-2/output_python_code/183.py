def solution():
    """A small poultry farm has 300 chickens, 200 turkeys and 80 guinea fowls. A strange, incurable disease hit the farm and every day the farmer lost 20 chickens, 8 turkeys and 5 guinea fowls. After a week, how many birds will be left in the poultry?"""
    chickens = 300
    turkeys = 200
    guinea_fowls = 80
    days = 7
    chicken_loss = 20
    turkey_loss = 8
    guinea_fowl_loss = 5
    total_loss_per_day = chicken_loss + turkey_loss + guinea_fowl_loss
    remaining_chickens = chickens - (total_loss_per_day * days)
    remaining_turkeys = turkeys - (total_loss_per_day * days)
    remaining_guinea_fowls = guinea_fowls - (total_loss_per_day * days)
    total_remaining_birds = remaining_chickens + remaining_turkeys + remaining_guinea_fowls
    result = total_remaining_birds
    return result

print(solution())