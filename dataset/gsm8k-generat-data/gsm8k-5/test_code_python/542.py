def solution():
    cakes_baked = 10 #Sara bakes 10 cakes everyday
    days_baked = 5 #Sara bakes for 5 days
    total_cakes_baked = cakes_baked * days_baked #Total cakes baked in 5 days
    cakes_eaten = 12 #Carol eats 12 cakes
    remaining_cakes = total_cakes_baked - cakes_eaten #Calculate remaining cakes
    frosting_per_cake = 2 #2 cans of frosting per cake

    #Calculate total cans of frosting needed for remaining cakes
    total_frosting = remaining_cakes * frosting_per_cake 
    result = total_frosting
    return result

print(solution())