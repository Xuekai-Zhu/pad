def solution():
    sandwiches_on_saturday = 2
    sandwiches_on_sunday = 1
    bread_per_sandwich = 2

    # Calculate total pieces of bread eaten by Sally
    total_bread = (sandwiches_on_saturday + sandwiches_on_sunday) * bread_per_sandwich
    result = total_bread
    return result

print(solution())