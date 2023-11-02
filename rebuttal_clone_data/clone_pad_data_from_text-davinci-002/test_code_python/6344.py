def solution():
    jars = 5
    juice_per_jar = 2
    jar_to_glass = 250
    total_juice = jars * juice_per_jar
    juice_available = total_juice * jar_to_glass
    glasses = juice_available / jar_to_glass
    result = glasses
    return result

print(solution())