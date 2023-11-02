def solution():
    forbidden_from_warfare = ["vows of nonviolence", "religious prohibition", "moral code"]
    monk_type = input("What type of monk are you referring to? ")
    if monk_type == "Buddhist Shaolin":
        result = "no"
    elif monk_type == "Knights Templar":
        result = "no"
    elif monk_type == "other type of monk":
        result = "it depends on their specific beliefs and practices"
    else:
        result = "I'm not sure, please provide more information"
    return result

print(solution())