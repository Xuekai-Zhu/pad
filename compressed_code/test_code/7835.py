def solution():
    
    total_flyers = 200
    flyers_passed_out = 42 + 67 + 51
    belinda_flyers = total_flyers - flyers_passed_out
    percentage = (belinda_flyers / total_flyers) * 100
    result = percentage
    return result

print(solution())