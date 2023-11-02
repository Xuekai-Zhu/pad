def solution():
    """A small poultry farm has 300 chickens, 200 turkeys and 80 guinea fowls. A strange, incurable disease hit the farm and every day the farmer lost 20 chickens, 8 turkeys and 5 guinea fowls. After a week, how many birds will be left in the poultry?"""
    chickens = 300
    turkeys = 200
    guinea_fowls = 80
    chickens_lost_per_day = 20
    turkeys_lost_per_day = 8
    guinea_fowls_lost_per_day = 5
    days_passed = 7
    chickens_left = chickens - (chickens_lost_per_day * days_passed)
    turkeys_left = turkeys - (turkeys_lost_per_day * days_passed)
    guinea_fowls_left = guinea_fowls - (guinea_fowls_lost_per_day * days_passed)
    total_birds_left = chickens_left + turkeys_left + guinea_fowls_left
    result = total_birds

print(solution())