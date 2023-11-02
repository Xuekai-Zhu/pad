def solution():
    """It is raining outside and Bill puts his empty fish tank in his yard to let it fill with rainwater. It starts raining at 1 pm. 2 inches of rainfall in the first hour. For the next four hours, it rains at a rate of 1 inch per hour. It then rains at three inches per hour for the rest of the day. If the fish tank is 18 inches tall, at what time will it be filled with rainwater."""
    tank_height = 18
    current_rainfall = 0
    current_time = 1
    time_to_fill = 0
    
    while current_rainfall < tank_height:
        if current_time == 1:
            current_rainfall += 2
            time_to_fill += 1
        elif current_time > 1 and current_time <= 5:
            current_rainfall += 1
            time_to_fill += 1
        else:
            current_rainfall += 3
            time_to_fill += 1
        
        current_time += 1
    
    result = time_to_fill
    
    return result

print(solution())