def solution():
    """Aliya and her classmates are sent by their teacher to the field to collect insects for science class study. The Boys collected 200 insects and the girls collected 300 insects. The teacher decided to divide the class equally into four groups that each get an equal number of insects so that each group could study together. What was the number of insects given to each group?"""
    # Define the number of insects collected by the boys and girls
    boys_insects = 200
    girls_insects = 300

    # Calculate the total number of insects collected
    total_insects = boys_insects + girls_insects

    # Calculate the number of insects each group gets
    insects_per_group = total_insects / 4

    # Round the result to the nearest whole number
    result = round(insects_per_group)
    return result

print(solution())