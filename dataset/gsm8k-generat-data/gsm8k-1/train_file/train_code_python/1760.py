def solution():
    """Kevin is a fruit vendor. He always sells a total of 50 crates of fruit per week. Last week he sold 13 crates of grapes, 20 crates of mangoes, and the rest were passion fruits. How many passion fruit crates did he sell?"""
    total_crates = 50
    grape_crates = 13
    mango_crates = 20
    passion_crates = total_crates - grape_crates - mango_crates
    result = passion_crates
    return result

print(solution())