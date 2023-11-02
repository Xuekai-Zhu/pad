def solution():
    # Calculate James' current age
    age_James = 37 - 15 
    
    # Calculate Janet's current age
    age_Janet = (age_James - 8) / 2
    
    # Calculate how many years ago Janet was born
    years_ago_Janet_born = age_James - age_Janet - 3
    
    # Calculate Susan's current age
    age_Susan = 3 + 8 + years_ago_Janet_born + 5
    
    result = age_Susan
    return result

print(solution())