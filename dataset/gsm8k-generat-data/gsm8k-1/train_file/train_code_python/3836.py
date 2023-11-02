def solution():
    """A pack of dogs found a pile of bones in the dumpster behind the butcher shop. One by one, the dogs crawled into the dumpster, grabbed a mouthful of bones, and ran off with their newfound treasure. In all, there were 5 dogs. The first dog carried off 3 bones. The second dog carried off 1 less bone than the first dog. The third dog carried off twice as many as the second dog. The fourth dog carried off one bone, and the fifth dog carried off twice the number of bones as the fourth dog carried, leaving no remaining bones in the dumpster. How many bones were in the original pile of bones?"""
    # First dog carried off 3 bones
    bones_remaining = bones_initial - 3
    # Second dog carried off 1 less bone than the first
    bones_remaining = bones_remaining - (3 - 1)
    # Third dog carried off twice as many as second
    bones_remaining = bones_remaining - ((3 - 1) * 2)
    # Fourth dog carried off one bone
    bones_remaining = bones_remaining - 1
    # Fifth dog carried off twice as many as fourth
    bones_remaining = bones_remaining - (1 * 2)
    result = bones_initial
    return result

print(solution())