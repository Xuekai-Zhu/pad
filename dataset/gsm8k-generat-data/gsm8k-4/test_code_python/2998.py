def solution():
    """As a freelancer, Katherine takes 20 hours to develop a website for her clients. Her junior, Naomi, takes 1/4 times more time to complete creating a similar website. If many clients required her to build their websites in a particular year, and she gave her junior 30 websites to develop, calculate the total number of hours Katherine's junior took to create the 30 websites."""
    # Define the time Katherine takes to develop a website
    katherine_time = 20

    # Calculate the time Naomi takes to develop a website
    naomi_time = katherine_time + (katherine_time * 1/4)

    # Calculate the total time Naomi takes to develop 30 websites
    total_time = naomi_time * 30

    # Return the result
    result = total_time
    return result

print(solution())