def solution():
    """Kevin is a fruit vendor. He always sells a total of 50 crates of fruit per week. Last week he sold 13 crates of grapes, 20 crates of mangoes, and the rest were passion fruits. How many passion fruit crates did he sell?"""
    # Define the total number of crates sold last week
    total_crates = 50

    # Define the number of crates of grapes and mangoes sold
    grape_crates = 13
    mango_crates = 20

    # Calculate the number of passion fruit crates sold
    passion_crates = total_crates - grape_crates - mango_crates

    # Display the number of passion fruit crates sold
    result = passion_crates
    return result

print(solution())