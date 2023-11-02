def solution():
    bonny_pairs = 13  # Bonny just bought her 13th pair of shoes
    becky_pairs = (bonny_pairs + 5) / 2  # Becky owns 5 less than twice as many pairs of shoes as Bonny owns
    bobby_pairs = 3 * becky_pairs  # Bobby has 3 times as many pairs of shoes as Becky has
    total_shoes = bonny_pairs + becky_pairs + bobby_pairs  # Total number of shoes among the three

    result = bobby_pairs * 2  # Convert the number of pairs to the number of shoes
    return result

print(solution())