def solution():
    amtrak_destinations = ["various locations"]
    moai_location = ["Easter Island"]
    if "Easter Island" in moai_location and "various locations" in amtrak_destinations:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())