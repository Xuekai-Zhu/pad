def solution():
    """In the city of Soda, there are exactly 23786 inhabitants. They include 8417 men and 9092 women. The rest of the population is made up of children. How many kids are there in Soda?"""
    total_population = 23786
    men_population = 8417
    women_population = 9092
    children_population = total_population - men_population - women_population
    result = children_population
    return result

print(solution())