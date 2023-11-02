def solution():
    # Calculate the total number of engines and the number of defective engines
    total_engines = 5 * 80  # 5 batches of 80 engines each
    defective_engines = total_engines / 4  # one fourth of the engines are defective

    # Calculate the number of non-defective engines
    nondefective_engines = total_engines - defective_engines

    result = nondefective_engines
    return result

print(solution())