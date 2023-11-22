def solution():
    
    # Define the number of boys and girls
    num_boys = 12
    num_girls = 12

    # Calculate the number of girls and boys who are on varsity
    num_girls_on_varsity = num_girls // 3
    num_boys_on_varsity = num_boys // 4

    # Calculate the total number of students who are on varsity
    total_on_varsity = num_girls_on_varsity + num_boys_on_varsity

    # Calculate the number of students who are not on varsity
    num_not_on_varsity = num_boys + num_girls - total_on_varsity

    # Display the number of students who are not on varsity
    result = num_not_on_varsity
    return result

print(solution())