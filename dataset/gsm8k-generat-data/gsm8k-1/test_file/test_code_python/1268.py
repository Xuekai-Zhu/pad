def solution():
    """Helen went on a trip through Germany. She booked a hotel for 3 nights and rode the bus 7 times during that trip. One night at the hotel was a cost of $80, and every bus trip was 10% of the price of one night at the hotel.
    How much did Helen pay for the hotel and bus travels during that trip?"""
    nights_at_hotel = 3
    cost_of_hotel_per_night = 80
    cost_of_one_bus_ride = cost_of_hotel_per_night * 0.10
    bus_rides = 7
    total_cost_of_bus_rides = cost_of_one_bus_ride * bus_rides
    total_cost_of_hotel = nights_at_hotel * cost_of_hotel_per_night
    total_cost = total_cost_of_hotel + total_cost_of_bus_rides
    result = total_cost
    return result

print(solution())