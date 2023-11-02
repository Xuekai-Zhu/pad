def solution():
    """
    A roadwork company is paving a newly constructed 16-mile road.
    They use a mixture of pitch and gravel to make the asphalt to pave the road.
    Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make.
    It takes three truckloads of asphalt to pave each mile of road.
    The company paved 4 miles of road on one day, then one mile less than double that on the second day.
    How many barrels of pitch will the company need to finish the remaining road on the third day?
    """
    total_miles = 16
    barrels_per_truck = 1
    gravel_per_truck = 2 / 5
    asphalt_per_truck = barrels_per_truck + 5 * gravel_per_truck

    day1_miles = 4
    day2_miles = (2 * day1_miles) - 1
    day3_miles = total_miles - day1_miles - day2_miles

    day1_trucks = day1_miles * 3
    day2_trucks = day2_miles * 3
    day3_trucks = day3_miles * 3

    total_trucks = day1_trucks + day2_trucks + day3_trucks
    total_barrels = total_trucks * barrels_per_truck

    result = total_barrels
    return result

print(solution())