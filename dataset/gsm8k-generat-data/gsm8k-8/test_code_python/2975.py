def solution():
    # Calculate how many red erasers Tanya has
    tanya_red_erasers = 20 / 2

    # Calculate how many erasers Rachel has
    rachel_erasers = (1/2) * tanya_red_erasers - 3

    # Calculate how many erasers Hanna has
    hanna_erasers = 2 * rachel_erasers

    result = hanna_erasers
    return result

print(solution())