def solution():
    num_vets = 1000
    puppy_recommendation_percentage = 0.2
    yummy_recommendation_percentage = 0.3

    # Calculate the number of vets who recommend Puppy Kibble
    num_puppy_recommendations = num_vets * puppy_recommendation_percentage

    # Calculate the number of vets who recommend Yummy Dog Kibble
    num_yummy_recommendations = num_vets * yummy_recommendation_percentage

    # Calculate the difference between the number of vets who recommend Yummy Dog Kibble and Puppy Kibble
    difference = num_yummy_recommendations - num_puppy_recommendations
    result = difference
    return result

print(solution())