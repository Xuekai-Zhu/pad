def solution():
    """20% of the vets in a state recommend Puppy Kibble. 30% recommend Yummy Dog Kibble. If there are 1000 vets in the state, how many more recommend Yummy Dog Kibble than Puppy Kibble?"""
    # Define the total number of vets and the percentages recommending each kibble
    total_vets = 1000
    puppy_percentage = 0.2
    yummy_percentage = 0.3

    # Calculate the number of vets recommending each kibble
    puppy_vets = total_vets * puppy_percentage
    yummy_vets = total_vets * yummy_percentage

    # Calculate the difference in the number of vets recommending each kibble
    diff = yummy_vets - puppy_vets

    # return the result
    result = diff
    return result

print(solution())