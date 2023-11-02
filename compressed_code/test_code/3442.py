def solution():
    
    total_guests = 200
    women_percentage = 40/100
    women_total = women_percentage * total_guests
    women_with_rabbit_ears = 80/100 * women_total
    men_total = total_guests - women_total
    men_with_rabbit_ears = 60/100 * men_total
    total_with_rabbit_ears = women_with_rabbit_ears + men_with_rabbit_ears
    result = total_with_rabbit_ears
    return result

print(solution())