def solution():
    """A small poultry farm has 300 chickens, 200 turkeys and 80 guinea fowls. A strange, incurable disease hit the farm and every day the farmer lost 20 chickens, 8 turkeys and 5 guinea fowls. After a week, how many birds will be left in the poultry?"""
    # Define the initial number of chickens, turkeys, and guinea fowls
    INITIAL_CHICKENS = 300
    INITIAL_TURKEYS = 200
    INITIAL_GUINEA_FOWLS = 80

    # Define the daily loss of chickens, turkeys, and guinea fowls
    DAILY_CHICKEN_LOSS = 20
    DAILY_TURKEY_LOSS = 8
    DAILY_GUINEA_FOWL_LOSS = 5

    # Calculate the number of chickens, turkeys, and guinea fowls left after a week
    chickens_left = INITIAL_CHICKENS - DAILY_CHICKEN_LOSS * 7
    turkeys_left = INITIAL_TURKEYS - DAILY_TURKEY_LOSS * 7
    guinea_fowls_left = INITIAL_GUINEA_FOWLS - DAILY_GUINEA_FOWL_LOSS * 7

    # Calculate the total number of birds left
    total_birds_left = chickens_left + turkeys_left + guinea_fowls_left

    # Return the result
    result = total_birds_left
    return result

print(solution())