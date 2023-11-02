def solution():
    """Nina has four times more math homework and eight times more reading homework than Ruby. If Ruby has six math homework and two reading homework, how much homework is Nina having altogether?"""
    # Define the ratios of Nina's homework to Ruby's homework
    MATH_RATIO = 4
    READING_RATIO = 8

    # Get the number of math and reading homework that Ruby has
    ruby_math = 6
    ruby_reading = 2

    # Calculate the number of math and reading homework that Nina has
    nina_math = ruby_math * MATH_RATIO
    nina_reading = ruby_reading * READING_RATIO

    # Calculate the total homework that Nina has
    total_homework = nina_math + nina_reading

    # Display the total homework that Nina has
    result = total_homework
    return result

print(solution())