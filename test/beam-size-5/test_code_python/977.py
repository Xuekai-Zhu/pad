def solution():
    
    thursday_crawfish = 3
    friday_crawfish = thursday_crawfish * 4
    saturday_crawfish = friday_crawfish / 2
    total_crawfish = thursday_crawfish + friday_crawfish + saturday_crawfish
    serving_size = 3
    servings = total_crawfish // serving_size
    result = servings
    return result

print(solution())