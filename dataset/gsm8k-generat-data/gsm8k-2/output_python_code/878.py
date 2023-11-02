def solution():
    """Jake amasses a fortune of 80 bitcoin. He donates 20 bitcoins to charity. He then gives half of all the bitcoins to his brother. After that, he triples the number of bitcoins he has. Then he donates another 10 coins. How many coins does he have?"""
    starting_bitcoins = 80
    donated_bitcoins = 20
    remaining_bitcoins = starting_bitcoins - donated_bitcoins
    half_bitcoins = remaining_bitcoins / 2
    new_bitcoins = half_bitcoins + remaining_bitcoins
    final_bitcoins = new_bitcoins * 3
    final_donation = 10
    total_bitcoins = final_bitcoins - final_donation
    result = total_bitcoins
    return result

print(solution())