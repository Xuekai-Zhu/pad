def solution():
    
    anna_candy_per_house = 14
    billy_candy_per_house = 11
    anna_houses = 60
    billy_houses = 75
    anna_total_candy = anna_candy_per_house * anna_houses
    billy_total_candy = billy_candy_per_house * billy_houses
    candy_difference = anna_total_candy - billy_total_candy
    result = candy_difference
    return result

print(solution())