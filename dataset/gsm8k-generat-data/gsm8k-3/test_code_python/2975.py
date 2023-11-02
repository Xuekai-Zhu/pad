def solution():
    """Hanna has twice as many erasers as Rachel. Rachel has three less than one-half as many erasers as Tanya has red erasers. If Tanya has 20 erasers, and half of them are red, how many erasers does Hanna have?"""
    # Define the number of erasers Tanya has
    tanya_erasers = 20

    # Calculate the number of red erasers Tanya has
    red_erasers = tanya_erasers / 2

    # Calculate the number of erasers Rachel has
    rachel_erasers = (red_erasers / 2) - 3

    # Calculate the number of erasers Hanna has
    hanna_erasers = rachel_erasers * 2

    # Display the number of erasers Hanna has
    result = hanna_erasers
    return result

print(solution())