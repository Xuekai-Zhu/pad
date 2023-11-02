def solution():
    
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