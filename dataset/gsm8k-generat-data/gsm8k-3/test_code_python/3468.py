def solution():
    """Big Joe is the tallest player on the basketball team.  He is one foot taller than Ben, who is one foot taller than Larry, who is one foot taller than Frank, who is half a foot taller than Pepe.  If Pepe is 4 feet six inches tall, how tall is Big Joe, in feet?"""
    # Convert Pepe's height to feet
    pepe_height = (4*12 + 6) / 12

    # Calculate Frank's height
    frank_height = pepe_height + 0.5

    # Calculate Larry's height
    larry_height = frank_height + 1

    # Calculate Ben's height
    ben_height = larry_height + 1

    # Calculate Big Joe's height
    joe_height = ben_height + 1

    # Display Big Joe's height in feet
    result = joe_height
    return result

print(solution())