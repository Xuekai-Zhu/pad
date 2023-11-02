def solution():
    tanya_red_erasers = 20/2  # half of Tanya's erasers are red
    rachel_erasers = (1/2 * tanya_red_erasers) - 3  # Rachel has three less than one-half as many erasers as Tanya has red erasers
    hanna_erasers = 2 * rachel_erasers  # Hanna has twice as many erasers as Rachel
    result = hanna_erasers
    return result

print(solution())