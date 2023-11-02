def solution():
    """The school is hosting a race after school. The winner is the person who runs the most laps around the school in 12 minutes. One lap around the school is 100 meters. The winner is awarded a gift certificate equal to $3.5 for every one hundred meters they run. The winner runs 24 laps around the school. On average, how much did they earn per minute?"""
    # Define the race time in minutes
    race_time = 12

    # Define the distance of one lap around the school
    lap_distance = 100

    # Define the number of laps the winner ran
    laps = 24

    # Calculate the total distance ran by the winner
    total_distance = lap_distance * laps

    # Calculate the total amount earned by the winner
    total_earned = total_distance * 0.035

    # Calculate the average earned per minute
    earned_per_minute = total_earned / race_time

    result = round(earned_per_minute, 2)
    return result

print(solution())