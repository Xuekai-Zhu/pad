def solution():
    # Define Mennonite beliefs about technology and TV usage
    uses_technology = True
    avoids_TV = True
    # Check if children in Mennonite homes would know about The Powerpuff Girls
    if uses_technology and avoids_TV:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())