def solution():
    # Calculate the number of math and reading homework Ruby has
    ruby_math = 6
    ruby_reading = 2

    # Calculate the number of math and reading homework Nina has
    nina_math = 4 * ruby_math
    nina_reading = 8 * ruby_reading

    # Calculate the total homework Nina has
    total_homework = nina_math + nina_reading
    result = total_homework
    return result

print(solution())