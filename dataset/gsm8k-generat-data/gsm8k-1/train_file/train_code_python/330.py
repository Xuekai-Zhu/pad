def solution():
    """A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?"""
    miles_paved_day_one = 4
    miles_paved_day_two = (2 * miles_paved_day_one) - 1
    total_miles_paved = miles_paved_day_one + miles_paved_day_two
    miles_left = 16 - total_miles_paved
    barrels_per_truckload = 5
    barrels_of_pitch_per_mile = 3 * barrels_per_truckload
    total_barrels_of_pitch = miles_left * barrels_of_pitch_per_mile
    result = total_barrels_of_pitch
    return result

print(solution())