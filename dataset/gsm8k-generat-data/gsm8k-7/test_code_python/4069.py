def solution():
    pounds_of_mix = 10
    num_links = 40
    links_eaten = 12
    
    # Calculate the total amount of sausage meat in pounds
    total_sausage = pounds_of_mix * num_links / num_links
    
    # Calculate the amount of sausage meat in ounces
    total_sausage_ounces = total_sausage * 16
    
    # Calculate the amount of sausage meat in the eaten links in ounces
    eaten_sausage_ounces = (links_eaten/num_links) * total_sausage_ounces
    
    # Calculate the remaining amount of sausage meat in ounces
    remaining_sausage_ounces = total_sausage_ounces - eaten_sausage_ounces
    
    result = remaining_sausage_ounces
    return result

print(solution())