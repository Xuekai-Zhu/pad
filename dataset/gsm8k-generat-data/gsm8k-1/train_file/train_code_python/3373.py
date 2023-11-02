def solution():
    """Aliya and her classmates are sent by their teacher to the field to collect insects for science class study. The Boys collected 200 insects and the girls collected 300 insects. The teacher decided to divide the class equally into four groups that each get an equal number of insects so that each group could study together. What was the number of insects given to each group?"""
    total_insects = 200 + 300
    groups = 4
    insects_per_group = total_insects // groups
    result = insects_per_group
    return result

print(solution())