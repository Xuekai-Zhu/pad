def solution():
    """James needs to get more toys for his doggie shelter. Each dog needs one toy. James currently has 4 toys on hand for 4 dogs, but there are 8 more dogs in the shelter now. After buying the toys, he went back to see that there are twice as many more dogs than when he left so he had to buy some more toys. When James came back yet again, 3 dogs were gone so he no longer needed those toys. How many toys in total does James need?"""
    initial_dogs = 4
    initial_toys = 4
    new_dogs = 8
    second_dogs = initial_dogs + new_dogs
    second_toys = second_dogs - initial_toys
    final_dogs = second_dogs - 3
    total_toys = final_dogs - initial_toys
    result = total_toys
    return result

print(solution())