def solution():
    tanya_red_erasers = 20 / 2  # Tanya has half of her 20 erasers as red erasers
    rachel_erasers = (tanya_red_erasers / 2) - 3  # Rachel has three less than one-half of Tanya's red erasers
    hanna_erasers = rachel_erasers * 2  # Hanna has twice as many erasers as Rachel

    result = hanna_erasers
    return result

print(solution())