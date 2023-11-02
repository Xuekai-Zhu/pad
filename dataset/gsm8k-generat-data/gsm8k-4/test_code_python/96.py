def solution():
    """James has a rainwater collection barrel. For each inch of rain he collects 15 gallons. On Monday it rained 4 inches and on Tuesday it rained 3 inches. He can sell water for $1.2 per gallon. How much money did he make from selling all the water?"""
    # Define the amount of rain collected on Monday and Tuesday
    monday_rain = 4
    tuesday_rain = 3

    # Calculate the total amount of water collected
    total_water = (monday_rain + tuesday_rain) * 15

    # Calculate the total amount of money made from selling the water
    total_money = total_water * 1.2

    # return the result
    result = total_money
    return result

print(solution())