def solution():
    lawns_mowed = 3
    lawns_price = 8
    figures_sold = 2
    figures_price = 9
    job_hours = 10
    job_rate = 5
    shoes_cost = ((lawns_mowed * lawns_price) + (figures_sold * figures_price) + (job_hours * job_rate))
    result = shoes_cost
    return result

print(solution())