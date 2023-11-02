def solution():
    # Define the number of vets in the state and the percentage recommending each kibble
    total_vets = 1000
    puppy_recommend_percentage = 0.20
    yummy_recommend_percentage = 0.30

    # Calculate the number of vets recommending each kibble
    puppy_recommend_count = total_vets * puppy_recommend_percentage
    yummy_recommend_count = total_vets * yummy_recommend_percentage

    # Calculate the difference in the number of vets recommending each kibble
    difference = yummy_recommend_count - puppy_recommend_count
    result = difference
    return result

print(solution())