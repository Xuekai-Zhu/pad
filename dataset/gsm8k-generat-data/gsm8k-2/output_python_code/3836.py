def solution():
    """A pack of dogs found a pile of bones in the dumpster behind the butcher shop. One by one, the dogs crawled into the dumpster, grabbed a mouthful of bones, and ran off with their newfound treasure. In all, there were 5 dogs. The first dog carried off 3 bones. The second dog carried off 1 less bone than the first dog. The third dog carried off twice as many as the second dog. The fourth dog carried off one bone, and the fifth dog carried off twice the number of bones as the fourth dog carried, leaving no remaining bones in the dumpster. How many bones were in the original pile of bones?"""
    fifth_dog = 2
    fourth_dog = 1
    third_dog = 2 * (fourth_dog - 1)
    second_dog = first_dog - 1
    first_dog = 3 + second_dog + third_dog + fourth_dog + fifth_dog
    total_bones = first_dog + second_dog + third_dog + fourth_dog + fifth_dog
    result = total_bones
    return result

print(solution())