import art
import game_data
import random

print(art.logo)
end_game = 0

score = 0
#print(element_a)

while end_game == 0:
    if score == 0:
        element_a = random.choice(game_data.data)
    element_b = random.choice(game_data.data)
    if element_a == element_b:
        element_b = random.choice(game_data.data)    
    print(f"Compare A: {element_a['name']}, a {element_a['description']}, from {element_a['country']}.")
    print(art.vs)
    print(f"Against B: {element_b['name']}, a {element_b['description']}, from {element_b['country']}.")
    selection = input("Who has more Instagram followers? Type A or B: ")
    if element_a['follower_count'] > element_b['follower_count'] and selection == "A":
        score += 1
        print(f"You're right! Current score: {score}")
        element_a = element_b
        
    elif element_b['follower_count'] > element_a['follower_count'] and selection == "B":
        score += 1
        print(f"You're right! Current score: {score}")
        element_a = element_b
        
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        end_game = 1
    
