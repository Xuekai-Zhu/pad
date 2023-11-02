def solution():
    """All people named Barry are nice, while only half of the people named Kevin are nice. Three-fourths of people named Julie are nice, while 10% of people named Joe are nice. If a crowd contains 24 people named Barry, 20 people named Kevin, 80 people named Julie, and 50 people named Joe, how many nice people are in the crowd?"""
    nice_barry = 24
    nice_kevin = 0.5 * 20
    nice_julie = 0.75 * 80
    nice_joe = 0.1 * 50
    total_nice_people = nice_barry + nice_kevin + nice_julie + nice_joe
    result = total_nice_people
    return result

print(solution())