def solution():
    """McDonald is planning to open up a farm that provides eggs to the community. In his local community, Sally needs 10 eggs, Ben needs 14 eggs, and Ked needs half of the number of eggs needed by Ben per week.
    In a month which has 4 weeks, how many eggs should McDonald's farm produce?"""
    sally_eggs_per_week = 10
    ben_eggs_per_week = 14
    ked_eggs_per_week = ben_eggs_per_week / 2
    eggs_per_week = sally_eggs_per_week + ben_eggs_per_week + ked_eggs_per_week
    eggs_per_month = eggs_per_week * 4
    result = eggs_per_month
    return result

print(solution())