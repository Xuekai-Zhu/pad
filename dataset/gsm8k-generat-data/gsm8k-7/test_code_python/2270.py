def solution():
    num_students = 25
    perc_girls = 60
    perc_boys = 100 - perc_girls
    perc_boys_basket = 40

    # Calculate the number of girls and boys in the class
    num_girls = (perc_girls / 100) * num_students
    num_boys = (perc_boys / 100) * num_students

    # Calculate the number of boys who don't like playing basketball
    num_boys_no_basket = num_boys * (100 - perc_boys_basket) / 100

    # Calculate the number of girls who like playing basketball
    num_girls_basket = 2 * num_boys_no_basket

    # Calculate the percentage of girls who like playing basketball
    perc_girls_basket = (num_girls_basket / num_girls) * 100
    result = perc_girls_basket
    return result

print(solution())