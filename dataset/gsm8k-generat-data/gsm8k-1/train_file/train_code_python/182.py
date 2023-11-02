def solution():
    """A small poultry farm has 300 chickens, 200 turkeys and 80 guinea fowls. A strange, incurable disease hit the farm and every day the farmer lost 20 chickens, 8 turkeys and 5 guinea fowls. After a week, how many birds will be left in the poultry?"""
    chicken_count = 300
    turkey_count = 200
    guinea_fowl_count = 80
    days = 7
    chicken_loss = 20
    turkey_loss = 8
    guinea_fowl_loss = 5
    total_loss_per_day = chicken_loss + turkey_loss + guinea_fowl_loss
    total_loss = total_loss_per_day * days
    chickens_left = chicken_count - (chicken_loss * days)
    turkeys_left = turkey_count - (turkey_loss * days)
    guinea_fowls_left = guinea_fowl_count - (guinea_fowl_loss * days)
    total_birds_left = chickens_left + turkeys_left + guinea_fowls_left
    result = total_birds_left
    return result

print(solution())