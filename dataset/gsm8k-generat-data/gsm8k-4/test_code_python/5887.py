def solution():
    """Nina has four times more math homework and eight times more reading homework than Ruby. If Ruby has six math homework and two reading homework, how much homework is Nina having altogether?"""
    # Define the number of math and reading homework for Ruby
    ruby_math_homework = 6
    ruby_reading_homework = 2

    # Calculate the number of math and reading homework for Nina
    nina_math_homework = 4 * ruby_math_homework
    nina_reading_homework = 8 * ruby_reading_homework

    # Calculate the total number of homework assignments for Nina
    total_homework = nina_math_homework + nina_reading_homework

    # Return the result
    result = total_homework
    return result

print(solution())