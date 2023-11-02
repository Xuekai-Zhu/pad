def solution():
    """Tim decides to cancel his cable subscription and get streaming services. He gets Netflix for $10 a month. Hulu and Disney Plus normally cost $10 a month each but he saves 20% for bundling. How much money does he save by cancelling his $60 cable package?"""
    netflix_cost = 10
    bundle_discount = 0.2
    bundled_services_cost = (10 + 10) - (10 + 10) * bundle_discount
    cable_package_cost = 60
    money_saved = cable_package_cost - bundled_services_cost - netflix_cost
    result = money_saved
    
    return result

print(solution())