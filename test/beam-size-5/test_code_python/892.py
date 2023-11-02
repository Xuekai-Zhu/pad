def solution():
    
    rental_frequency = 10
    rental_duration = 3
    hourly_rate = 25
    payment = 500
    total_rental_duration = rental_frequency * rental_duration * rental_duration
    total_rental_cost = total_rental_duration * hourly_rate
    profit = total_rental_cost - payment
    result = profit
    return result

print(solution())