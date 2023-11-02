def solution():
    """Tiffany is looking at a lake full of turtles. The turtles are 60% female and the rest are male. Of the males, 1 in 4 has stripes. Of the ones with stripes, 4 are babies, while 60% are adults. How many turtles are in the lake?"""
    total_turtles = 100  # Assume there are 100 turtles for easy calculation
    females = total_turtles * 0.6
    males = total_turtles - females
    striped_males = males / 4
    baby_striped_males = 4
    adult_striped_males = striped_males * 0.6
    total_adult_males = males - baby_striped_males - striped_males
    total_adult_turtles = total_adult_males + (females * 0.6) + adult_striped_males
    result = total_turtles
    
    return result

print(solution())