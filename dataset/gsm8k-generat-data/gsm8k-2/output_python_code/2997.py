def solution():
    """As a freelancer, Katherine takes 20 hours to develop a website for her clients. Her junior, Naomi, takes 1/4 times more time to complete creating a similar website. If many clients required her to build their websites in a particular year, and she gave her junior 30 websites to develop, calculate the total number of hours Katherine's junior took to create the 30 websites."""
    katherine_time = 20
    naomi_time = katherine_time * (5/4) # 1/4 more time than Katherine
    num_websites = 30
    naomi_total_time = naomi_time * num_websites
    result = naomi_total_time
    return result

print(solution())