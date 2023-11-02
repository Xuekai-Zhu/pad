def solution():
    """Max likes to collect model trains. He asks for one for every birthday of his, and asks for two each Christmas. Max always gets the gifts he asks for, and asks for these same gifts every year for 5 years. At the end of the 5 years, his parents give him double the number of trains he already has. How many trains does Max have now?"""
    trains = 0
    for i in range(1, 6):
        trains += i + (2 * 2)  # 1 train for birthday + 2 trains for Christmas
    total_trains = trains * 2  # double the number of trains after 5 years
    result = total_trains
    return result

print(solution())