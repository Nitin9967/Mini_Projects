import art
import game_data
import random

i = 0  # Score counter


def get_details(index):
    """Returns details of a person from game_data."""
    return (game_data.data[index]['name'],
            game_data.data[index]['description'],
            game_data.data[index]['country'],
            game_data.data[index]['follower_count'])


# Main game loop
for _ in range(100):
    print(art.logo)

    # Select two unique random indices
    List_index, List_index2 = random.sample(range(50), 2)

    # Fetch details for both choices
    name, description, country, follower_A = get_details(List_index)
    print(f"Compare A: {name}, a {description}, from {country}.")

    print(art.vs)

    name, description, country, follower_B = get_details(List_index2)
    print(f"Compare B: {name}, a {description}, from {country}.")

    # Get user input
    foll = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check user choice and update score
    if foll == 'a' and follower_A > follower_B:
        i += 1
        print(f"You're right! Current score: {i}")
    elif foll == 'b' and follower_B > follower_A:
        i += 1
        print(f"You're right! Current score: {i}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {i}")
        break
