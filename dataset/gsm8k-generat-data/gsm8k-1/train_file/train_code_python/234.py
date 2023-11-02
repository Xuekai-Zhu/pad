def solution():
    """Max likes to collect model trains. He asks for one for every birthday of his, and asks for two each Christmas. Max always gets the gifts he asks for, and asks for these same gifts every year for 5 years. At the end of the 5 years, his parents give him double the number of trains he already has. How many trains does Max have now?"""
    trains_per_year = 1 + 2 + 1
    total_trains = trains_per_year * 5
    double_trains = total_trains * 2
    result = double_trains
    return result

print(solution())