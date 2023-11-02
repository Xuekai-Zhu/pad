def solution():
    hours_per_day = 24
    spider_hours = 5
    spider_flies = 9

    # Calculate the spider's efficiency per hour
    spider_efficiency = spider_flies / spider_hours

    # Calculate the total number of flies the spider would catch in 30 hours
    flies_in_30_hours = spider_efficiency * 30

    result = flies_in_30_hours
    return result

print(solution())