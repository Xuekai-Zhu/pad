def solution():
    """The total number of dogs at an animal rescue center is 200. Mr. Tanner, the manager at the rescue center, gets a call that 100 dogs at another rescue center are to be moved because of weather problems. He agrees to bring the dogs to his rescue center, and after one week, gives out 40 animals for adoption. After a month, 60 more dogs were adopted by dog lovers. What's the total number of remaining animals in the adoption center after the last adoptions?"""
    # Define the initial number of dogs
    initial_dogs = 200

    # Define the number of dogs moved from the other center
    moved_dogs = 100

    # Define the number of dogs given for adoption after one week
    adopted_week1 = 40

    # Define the number of dogs adopted after a month
    adopted_month1 = 60

    # Calculate the remaining number of dogs
    remaining_dogs = initial_dogs + moved_dogs - adopted_week1 - adopted_month1

    # Display the remaining number of dogs
    result = remaining_dogs
    return result

print(solution())