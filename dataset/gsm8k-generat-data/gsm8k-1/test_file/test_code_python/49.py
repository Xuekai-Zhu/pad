def solution():
    """A mechanic charges different rates to repair the tires of trucks and cars. For each truck tire that is repaired, the mechanic will charge $60 and for each car tire that is repaired, the mechanic will charge $40. On Thursday, the mechanic repairs 6 truck tires and 4 car tires. On Friday, the mechanic repairs 12 car tries and doesn't repair any truck tires. How much more revenue did the mechanic earn on the day with higher revenue?"""
    truck_tire_repair_fee = 60
    car_tire_repair_fee = 40
    thursday_trucks_repaired = 6
    thursday_cars_repaired = 4
    friday_trucks_repaired = 0
    friday_cars_repaired = 12
    
    thursday_revenue = (thursday_trucks_repaired * truck_tire_repair_fee) + (thursday_cars_repaired * car_tire_repair_fee)
    friday_revenue = (friday_trucks_repaired * truck_tire_repair_fee) + (friday_cars_repaired * car_tire_repair_fee)
    
    higher_revenue = max(thursday_revenue, friday_revenue)
    lower_revenue = min(thursday_revenue, friday_revenue)
    
    result = higher_revenue - lower_revenue
    return result

print(solution())