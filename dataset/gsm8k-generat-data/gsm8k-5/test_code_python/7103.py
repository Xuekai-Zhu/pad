def solution():
    single_balloon_price = 0.5  # One balloon costs $0.5
    pack_price = 3  # A pack of 10 balloons costs $3
    balloons_per_pack = 10  # There are 10 balloons in each pack
    total_balloons = 14  # Harry wants to bring 14 balloons to the party

    # Calculate the total cost of buying individual balloons
    individual_balloon_count = total_balloons % balloons_per_pack  # Calculate how many individual balloons Harry needs
    individual_balloon_cost = individual_balloon_count * single_balloon_price

    # Calculate the total cost of buying packs of balloons
    pack_count = total_balloons // balloons_per_pack  # Calculate how many packs of balloons Harry needs
    pack_cost = pack_count * pack_price

    # Calculate the total cost of all balloons
    total_cost = individual_balloon_cost + pack_cost
    result = total_cost
    return result

print(solution())