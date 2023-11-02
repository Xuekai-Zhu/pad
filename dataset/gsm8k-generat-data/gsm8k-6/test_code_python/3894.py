def solution():
    # Calculate the number of miles Tony drives in a week
    weekly_miles = 50 * 5  # Tony drives 50 miles round trip to work 5 days a week

    # Calculate the number of gallons of gas Tony uses in a week
    weekly_gallons = weekly_miles / 25  # Tony's car gets 25 miles to the gallon, so he uses one gallon of gas for every 25 miles he drives

    # Calculate the cost of gas for one week
    weekly_cost = weekly_gallons * 2  # Tony fills up at the local gas station for $2 a gallon

    # Calculate the cost of gas for four weeks
    total_cost = weekly_cost * 4

    result = total_cost
    return result

print(solution())