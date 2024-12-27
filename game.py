import time
import os

class DetectiveGame:
    def __init__(self):
        self.inventory = []
        self.clues = []
        self.suspects = {
            "Maid": "An anxious young woman who claims to have found the body.",
            "Butler": "A stern man with a spotless alibi.",
            "Gardner": "A gruff individual who seems nervous around the police."
        }
        self.game_over = False

    def slow_print(self, text, delay=0.05):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    def start_game(self):
        self.slow_print("Detective, you have been called to investigate in an old cottage house.")
        self.slow_print("The victim is Mr. Wilfred, a wealthy landowner. Let the investigation begin.\n")
        self.main_menu()

    def main_menu(self):
        while not self.game_over:
            self.slow_print("What would you like to do?\n1. Inspect the crime scene\n2. Interrogate a supect\n3. Check inventory\n4. Deduce the culprit\n5. Exit the game")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.inspect_crime_scene()
            elif choice == "2":
                self.interrogae_suspect()
            elif choice == "3":
                self.check_inventory()
            elif choice == "4":
                self.deduce_culprit()
            elif choice == "5":
                self.slow_print("Goodbye, Detective.")
                self.game_over = True
            else:
                self.slow_print("Invalid choice. Try again.")

    def inspect_crime_scene(self):
        self.slow_print("You enter the study where Mr. Wilfred's body was found. ")
        self.slow_print("The room is in disarray. Books are scattered, and a glass of wine is spilled on the floor.")
        self.slow_print("Where would you like to inspect?\n1. The body\n2. The desk\n3. The wine of glass\n4. Return to the main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.slow_print("The victim has a stab wound in his chest.His watch stopped at 10:15 PM.")
            self.clues.append("Time of death: 10:15 PM")
        elif choice == "2":
            self.slow_print("The desk drawer is locked. Perhaps you can find a key.")
        elif choice == "3":
            self.slow_print("The wine glass has a faint fingerprint. You bag it as evidence.")
            self.inventory.append("Fingerprint on wine glass")
        elif choice == "4":
            return
        else:
            self.slow_print("Invalid choice. Try again.")

    def interrogate_suspect(self):
        self.slow_print("Who would you like to interrogate?")
        for idx, suspect in enumerate(self.suspects, 1):
            self.slow_print(f"{idx}. {suspect} - {self.suspects[suspect]}")
            self.slow_print(f"{len(self.suspects) + 1}. Return to the main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.slow_print("The maid says she found the body at 10:30 PM when bringing tea.")
                self.clues.append("Maid's testimony: Found body at 10:30 PM")
            elif choice == "2":
                self.slow_print("The butler insists he was cleaning the silverware in the kitchen all evening")
            elif choice == "3":
                self.slow_print("The gardener claims was pruning roses but hesitates whed asked about the time.")
            elif choice == str(len(self.suspects) + 1):
                return
            else:
                self.slow_print("Invalid choice. Try again.")

    def check_inventory(self):
        self.slow_print("Inventory:")
        if self.inventory:
            for item in self.inventory:
                self.slow_print(f"- {item}")
        else:
            self.slow_print("Your inventory is empty.")

        self.slow_print("Clues:")
        if self.clues:
            for clue in self.clues:
                self.slow_print(f" - {clue}")
        else:
            self.slow_print("You have no clues yet.")

    def deduce_culprit(self):
        self.slow_print("Based on your investigation, who do you accuse of the murder?")
        for idx, suspect in enumerate(self.suspects, 1):
            self.slow_print(f"{idx}. {suspect}")
        self.slow_print(f"{len(self.suspects) + 1}. Return to the main menu")
        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            suspect = list(self.suspects.keys())[int(choice) - 1]
            self.end_game(suspect)
        elif choice == str(len(self.suspects) + 1):
            return
        else:
            self.slow_print("Invalid choice. Try again.")

    def end_game(self, suspect):
        if suspect == "Gardner" and "Fingerprint on wine glass" in self.inventory:
            self.slow_print(f"Congratulations, Detective! Youe correcly deduced that the {suspect} was the murderer.")
        else:
            self.slow_print(f"Unfortunately, Detective, you accused the wrong person. The true culprit remains free.")
        self.game_over = True

    def clear_screen():
        # For Windows
        if os.name == "nt":
            os.system("cls")
        # For MacOS and Linux
        else:
            os.system("Clear")

if __name__ == "__main__":
    os.system("cls")
    game = DetectiveGame()
    # game.clear_screen()
    game.start_game()
    