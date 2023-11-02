def solution():
    """20% of the vets in a state recommend Puppy Kibble. 30% recommend Yummy Dog Kibble. If there are 1000 vets in the state, how many more recommend Yummy Dog Kibble than Puppy Kibble?"""
    # Define the total number of vets in the state
    total_vets = 1000

    # Calculate the number of vets recommending Puppy Kibble
    pups_vets = total_vets * 0.2

    # Calculate the number of vets recommending Yummy Dog Kibble
    yummy_vets = total_vets * 0.3

    # Calculate the difference in the number of vets recommending each brand
    diff = yummy_vets - pups_vets

    # Display the difference in the number of vets recommending each brand
    result = diff
    return result

print(solution())