def solution():
    num_of_men = 30  # There are 30 men on the plane
    num_of_women = 30  # Since the number of men and women are equal, there are also 30 women on the plane
    total_passenger = 80  # There are a total of 80 passengers on the plane
    num_of_children = total_passenger - num_of_men - num_of_women  # The rest of the passengers are children
    result = num_of_children
    return result

print(solution())