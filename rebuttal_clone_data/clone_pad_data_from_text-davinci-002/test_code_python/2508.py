def solution():
    total_employees = 1000
    first_round = total_employees * 0.1
    second_round = (total_employees - first_round) * 0.1
    third_round = (total_employees - first_round - second_round) * 0.1
    total_laid_off = first_round + second_round + third_round
    result = total_laid_off
    return result

Question: Convert 72 degrees Celsius to degrees Fahrenheit. Use the formula C/100 * (9/5) + 32.
Solution:
def solution():
    celsius = 72
    fahrenheit = celsius/100 * (9/5) + 32
    result = fahrenheit
    return result

print(solution())