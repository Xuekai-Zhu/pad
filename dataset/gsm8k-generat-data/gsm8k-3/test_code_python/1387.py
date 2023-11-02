def solution():
    """John has 54 pieces of gum, Cole has 45 pieces of gum and Aubrey has no pieces of gum. They decide to share the gum equally between the 3 of them. How many pieces of gum will each one get?"""
    # Define the number of gum pieces for John and Cole
    john_gum = 54
    cole_gum = 45

    # Calculate the total number of gum pieces
    total_gum = john_gum + cole_gum

    # Calculate the gum pieces each person will get
    share_gum = total_gum // 3

    # Display the number of gum pieces each person will get
    result = share_gum
    return result

print(solution())