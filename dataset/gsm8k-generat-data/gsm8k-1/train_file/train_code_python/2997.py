def solution():
    """As a freelancer, Katherine takes 20 hours to develop a website for her clients.
    Her junior, Naomi, takes 1/4 times more time to complete creating a similar website.
    If many clients required her to build their websites in a particular year,
    and she gave her junior 30 websites to develop,
    calculate the total number of hours Katherine's junior took to create the 30 websites."""
    katherine_hours_per_website = 20
    naomi_multiplier = 1.25
    naomi_hours_per_website = katherine_hours_per_website * naomi_multiplier
    
    num_websites = 30
    
    total_hours = naomi_hours_per_website * num_websites
    
    result = total_hours
    
    return result

print(solution())