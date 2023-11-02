def solution():
    #Calculate the number of scientists from Europe and Canada
    euro_scientists = 70 // 2
    canada_scientists = 70 // 5
    
    #Calculate the number of scientists from the USA
    usa_scientists = 70 - euro_scientists - canada_scientists
    
    result = usa_scientists
    return result

print(solution())