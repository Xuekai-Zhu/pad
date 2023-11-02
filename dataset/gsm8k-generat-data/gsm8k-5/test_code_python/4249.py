def solution():
    first_jar = 80  # First jar has 80 marbles
    second_jar = 2 * first_jar  # Second jar has twice the amount of marbles in the first jar
    third_jar = first_jar / 4  # Third jar has 1/4 the amount of marbles in the first jar

    # Calculate the total number of marbles Courtney has
    total_marbles = first_jar + second_jar + third_jar
    result = total_marbles
    return result

print(solution())