def solution():
    total_commute = 21  # Total one-way commute is 21 miles
    gas_cost = 2.5  # Gas costs $2.5 per gallon
    car_mileage = 30  # Carson's car gets 30 miles per gallon
    num_friends = 5  # Carson provides a carpool for 5 friends
    work_days_per_week = 5  # They commute to work 5 days a week
    weeks_per_month = 4  # They commute to work 4 weeks a month

    # Calculate the total number of gallons used for each trip
    gallons_per_trip = total_commute / car_mileage

    # Calculate the total cost of gas for each trip
    cost_per_trip = gallons_per_trip * gas_cost

    # Calculate the total cost of gas for each friend per week
    cost_per_friend_per_week = cost_per_trip / num_friends

    # Calculate the total cost of gas for each friend per month
    cost_per_friend_per_month = cost_per_friend_per_week * work_days_per_week * weeks_per_month

    result = cost_per_friend_per_month
    return result

print(solution())