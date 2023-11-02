def solution():
    # Calculate the number of girls and boys in the class
    total_students = 25
    girls = total_students * 0.6
    boys = total_students - girls

    # Calculate the number of boys who like and don't like playing basketball
    boys_like_basketball = boys * 0.4
    boys_dont_like_basketball = boys - boys_like_basketball

    # Calculate the number of girls who like playing basketball
    girls_like_basketball = 2 * boys_dont_like_basketball

    # Calculate the percentage of girls who like playing basketball
    percentage_girls_like_basketball = (girls_like_basketball / girls) * 100
    result = percentage_girls_like_basketball
    return result

print(solution())