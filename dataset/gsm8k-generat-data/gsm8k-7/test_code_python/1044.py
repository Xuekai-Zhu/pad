def solution():
    num_ads = 5
    ad_length = 3  # in minutes
    ad_cost_per_minute = 4000

    # Calculate the total length of all advertisements
    total_ad_length = num_ads * ad_length

    # Calculate the total cost of transmitting the advertisements
    total_cost = total_ad_length * ad_cost_per_minute
    result = total_cost
    return result

print(solution())