def solution():
    """Jack goes hunting 6 times a month. The hunting season lasts for 1 quarter of the year. He catches 2 deers each time he goes hunting and they weigh 600 pounds each. He keeps half the weight of deer a year. How much deer does he keep in pounds?"""
    
    # Define the number of times Jack goes hunting per month
    hunting_per_month = 6
    
    # Define the duration of hunting season in months
    hunting_season_in_months = 3
    
    # Define the number of deers caught each time
    deers_caught_per_hunt = 2
    
    # Define the weight of each deer caught
    deer_weight = 600
    
    # Calculate the total number of deers caught in a hunting season
    total_deers_caught = hunting_per_month * hunting_season_in_months * deers_caught_per_hunt
    
    # Calculate the total weight of all the deers caught
    total_deer_weight = total_deers_caught * deer_weight
    
    # Calculate the weight of deers that Jack keeps
    deer_weight_kept = total_deer_weight / 2
    
    # Return the result in pounds
    result = deer_weight_kept
    return result

print(solution())