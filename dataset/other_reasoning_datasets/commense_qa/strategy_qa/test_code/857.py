def solution():
    # Define Jehovah's Witnesses' beliefs on smoking
    jehovahs_witness_belief = "strictly forbids tobacco and smoking"
    # Check if the Caterpillar's smoking contradicts their beliefs
    if "smoking" in jehovahs_witness_belief and "smoking" in "blows rings of smoke from a large pipe":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())