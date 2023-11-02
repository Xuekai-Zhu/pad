def solution():
    springfield_population = 482653  # Springfield's population is 482,653
    greenville_population = springfield_population - 119666  # Greenville has 119,666 fewer people than Springfield
    total_population = springfield_population + greenville_population  # Calculate the total population of both cities
    result = total_population
    return result

print(solution())