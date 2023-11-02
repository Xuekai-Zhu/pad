def solution():
    """A water tank has a capacity of 4000 gallons. Mack connects a pipe to the tank that fills the tank with water at the rate of 10 gallons per hour. How long will it take to fill the tank to 3/4 of its capacity?"""
    tank_capacity = 4000
    fill_rate = 10
    three_fourths_capacity = 0.75 * tank_capacity
    time_to_fill = (three_fourths_capacity / fill_rate)
    result = time_to_fill
    return result

print(solution())