def solution():
    """Kimberly loves gumballs and will trade almost anything she owns for them. A friend knows that Kim has a bunch of shiny new earrings that she loves. She agrees to give Kim 9 gumballs for each pair of earrings. On the first day, Kim brings her 3 pairs of earrings. On the second she brings her twice as many. On the third day, she brings 1 less than she brought on the second day. If Kim eats 3 gumballs a day, how many days will the gumballs last?"""

    earrings = [3, 6, 5]
    gumballs_per_earring = 9
    total_gumballs = sum([earring * gumballs_per_earring for earring in earrings])
    gumballs_eaten = 3 * len(earrings)
    days_last = total_gumballs // gumballs_eaten
    
    return days_last

print(solution())