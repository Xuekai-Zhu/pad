def solution():
    # Calculate the number of girls and boys in the class
    num_girls = int(0.6 * 25)
    num_boys = 25 - num_girls

    # Calculate the number of boys who like playing basketball
    num_boys_basketball = int(0.4 * num_boys)

    # Calculate the number of boys who don't like playing basketball
    num_boys_no_basketball = num_boys - num_boys_basketball

    # Calculate the number of girls who like playing basketball
    num_girls_basketball = 2 * num_boys_no_basketball

    # Calculate the total number of students who like playing basketball
    total_basketball = num_boys_basketball + num_girls_basketball

    # Calculate the percentage of girls who like playing basketball
    percentage_girls_basketball = (num_girls_basketball / num_girls) * 100

    result = percentage_girls_basketball
    return result

print(solution())