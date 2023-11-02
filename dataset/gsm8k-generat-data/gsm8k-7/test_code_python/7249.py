def solution():
    limit = 1000
    sat_words = 450
    sun_words = 650
    
    # Calculate the total number of words Vinnie wrote
    total_words = sat_words + sun_words
    
    # Calculate the number of words Vinnie exceeded the limit by
    exceeded_words = total_words - limit
    
    result = exceeded_words
    return result

print(solution())