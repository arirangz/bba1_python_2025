import pickle
games = []
def load_games():
    with open("games.pkl", "rb") as file:
        games = pickle.load(file)
        if games:
            for game in games:
                print(f"Name: {game["name"]} Editor: {game["editor"]}")
    
def save_game():
    name = input("Enter game name")
    editor = input("Enter the editor name")
    game = {"name": name, "editor": editor}
    games.append(game)
    with open("games.pkl", "wb") as file:
        pickle.dump(games, file)
    
def display_menu():
    while True:
        print("Menu")
        print("To add a game press A")
        print("To list games press L")
        print("To quit press Q")
        
        choice = input("Enter your choice: ")
        
        if choice == "A":
            save_game()
        elif choice == "L":
            load_games()
        elif choice == "Q":
            break

if __name__ == "__main__":
    display_menu()