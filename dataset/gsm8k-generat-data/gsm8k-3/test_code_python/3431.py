def solution():
    """The school is hosting a race after school. The winner is the person who runs the most laps around the school in 12 minutes.  One lap around the school is 100 meters. The winner is awarded a gift certificate equal to $3.5 for every one hundred meters they run. The winner runs 24 laps around the school. On average, how much did they earn per minute?"""
    # Define the laps run by the winner and lap distance
    LAPS = 24
    LAP_DISTANCE = 100

    # Calculate the distance travelled by winner in 12 minutes
    distance_travelled = LAPS * LAP_DISTANCE

    # Calculate the total amount earned by winner
    amount_earned = distance_travelled * (3.5 / LAP_DISTANCE)

    # Calculate the average amount earned per minute
    amount_per_minute = amount_earned / 12

    result = amount_per_minute
    return result

print(solution())