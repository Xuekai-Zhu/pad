def solution():
    # Calculate the total cost of Michelle's ride
    ride_fee = 2  # fee paid as soon as entering the taxi
    distance = 4  # distance traveled in miles
    per_mile_charge = 2.5  # charge per mile traveled
    total_charge = ride_fee + (per_mile_charge * distance)
    
    result = total_charge
    return result

print(solution())