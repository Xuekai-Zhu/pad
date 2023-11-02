def solution():
    """Morgan's dad said that she had $90 budgeted for her birthday party. She wants to make sure she and her friends all get to play one round of mini-golf, have $5 in arcade tokens, and get to ride the go-karts twice. A round of mini-golf is $5. The Go-karts cost $10 a ride. How many friends can she invite?"""
    budget = 90
    mini_golf_cost = 5
    arcade_tokens_cost = 5
    go_kart_cost_per_ride = 10
    go_kart_rides = 2
    total_cost_per_person = mini_golf_cost + arcade_tokens_cost + (go_kart_cost_per_ride * go_kart_rides)
    num_friends = int((budget - 5) / total_cost_per_person)
    result = num_friends
    return result

print(solution())