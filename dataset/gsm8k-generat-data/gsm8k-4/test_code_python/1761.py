def solution():
    """Kevin is a fruit vendor. He always sells a total of 50 crates of fruit per week. Last week he sold 13 crates of grapes, 20 crates of mangoes, and the rest were passion fruits. How many passion fruit crates did he sell?"""
    # Define the total number of fruit crates sold
    total_crates = 50

    # Define the number of grape and mango crates sold
    grape_crates = 13
    mango_crates = 20

    # Calculate the number of passion fruit crates sold
    passion_crates = total_crates - grape_crates - mango_crates

    # return the result
    result = passion_crates
    return result

print(solution())