def solution():
    bonny_pairs = 13  # number of pairs of shoes Bonny bought
    becky_pairs = (bonny_pairs + 5)/2  # number of pairs of shoes Becky owns
    bobby_pairs = 3 * becky_pairs  # number of pairs of shoes Bobby owns
    bobby_shoes = bobby_pairs * 2  # number of shoes Bobby owns (1 pair of shoes = 2 shoes)

    result = bobby_shoes
    return result

print(solution())