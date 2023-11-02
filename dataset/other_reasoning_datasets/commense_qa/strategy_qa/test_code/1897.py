def solution():
    movie_name = "Pirates of the Caribbean"
    character_name = "Captain Teague"
    occupation = "captain of a boat"
    if movie_name in ["Pirates of the Caribbean: At World's End", "Pirates of the Caribbean: On Stranger Tides"] and character_name == "Captain Teague" and occupation in ["captain of a boat", "pirate captain"]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())