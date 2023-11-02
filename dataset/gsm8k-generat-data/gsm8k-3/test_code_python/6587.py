def solution():
    """A school has 100 students. Half of the students are girls, the other half are boys. 
    20% of the girls have dogs at home and 10% of the boys have dogs at home. How many students own dogs?"""
    
    # Define the number of students and the percentage of girls and boys
    NUM_STUDENTS = 100
    PERCENT_GIRLS = 0.5
    PERCENT_BOYS = 0.5

    # Calculate the number of girls and boys
    num_girls = int(NUM_STUDENTS * PERCENT_GIRLS)
    num_boys = int(NUM_STUDENTS * PERCENT_BOYS)

    # Calculate the number of girls and boys who have dogs
    num_girls_with_dogs = int(num_girls * 0.2)
    num_boys_with_dogs = int(num_boys * 0.1)

    # Calculate the total number of students with dogs
    total_dog_owners = num_girls_with_dogs + num_boys_with_dogs

    # Display the total number of students with dogs
    result = total_dog_owners
    return result

print(solution())