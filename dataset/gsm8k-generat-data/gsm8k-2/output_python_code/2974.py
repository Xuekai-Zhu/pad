def solution():
    """Hanna has twice as many erasers as Rachel. Rachel has three less than one-half as many erasers as Tanya has red erasers. If Tanya has 20 erasers, and half of them are red, how many erasers does Hanna have?"""
    tanya_red_erasers = 20 / 2
    rachel_erasers = (tanya_red_erasers / 2) - 3
    hanna_erasers = rachel_erasers * 2
    result = hanna_erasers
    return result

print(solution())