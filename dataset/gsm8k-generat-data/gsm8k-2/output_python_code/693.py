def solution():
    """If one fourth of the engines are defective, and there are 5 batches of 80 engines each. How many engines are not defective?"""
    total_engines = 5 * 80
    defective_engines = total_engines // 4
    valid_engines = total_engines - defective_engines
    result = valid_engines
    return result

print(solution())