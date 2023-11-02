def solution():
    captcha_definition = "Completely Automated Public Turing test to tell Computers and Humans Apart"
    words = captcha_definition.split()
    for word in words:
        if word == word[::-1]:
            result = "yes"
            break
        else:
            result = "no"
    return result

print(solution())