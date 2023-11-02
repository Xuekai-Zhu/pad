def solution():
    """A small poultry farm has 300 chickens, 200 turkeys and 80 guinea fowls. A strange, incurable disease hit the farm and every day the farmer lost 20 chickens, 8 turkeys and 5 guinea fowls. After a week, how many birds will be left in the poultry?"""
    # Define the initial number of chickens, turkeys and guinea fowls
    chickens = 300
    turkeys = 200
    guinea_fowls = 80

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Define the daily loss of chickens, turkeys and guinea fowls
    daily_loss_chickens = 20
    daily_loss_turkeys = 8
    daily_loss_guinea_fowls = 5

    # Calculate the total weekly loss of chickens, turkeys and guinea fowls
    weekly_loss_chickens = daily_loss_chickens * DAYS_IN_WEEK
    weekly_loss_turkeys = daily_loss_turkeys * DAYS_IN_WEEK
    weekly_loss_guinea_fowls = daily_loss_guinea_fowls * DAYS_IN_WEEK

    # Subtract the weekly loss from the initial number of chickens, turkeys and guinea fowls
    chickens_left = chickens - weekly_loss_chickens
    turkeys_left = turkeys - weekly_loss_turkeys
    guinea_fowls_left = guinea_fowls - weekly_loss_guinea_fowls

    # Calculate the total number of birds left in the poultry
    total_birds_left = chickens_left + turkeys_left + guinea_fowls_left

    # Return the result
    result = total_birds_left
    return result

print(solution())