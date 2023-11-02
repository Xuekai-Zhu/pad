Assuming each sausage link is the same size and contains the same amount of meat:

def solution():
    pounds_of_meat = 10
    sausage_links = 40
    eaten_links = 12
    remaining_links = sausage_links - eaten_links
    
    # Assuming each link contains the same amount of meat, divide the total amount of meat by the number of links
    ounces_per_link = (pounds_of_meat * 16) / sausage_links
    remaining_ounces_of_meat = ounces_per_link * remaining_links
    
    result = remaining_ounces_of_meat
    return result

print(solution())