def solution():
    """A real estate agent has spent $5 on each newspaper ad and spent $75 on each television ad. He bought 50 newspaper ads and 15 television ads. How much did the real estate agent spend on buying all the ads?"""
    newspaper_cost = 5
    tv_cost = 75
    num_newspaper_ads = 50
    num_tv_ads = 15
    total_cost = (newspaper_cost * num_newspaper_ads) + (tv_cost * num_tv_ads)
    result = total_cost
    return result

print(solution())