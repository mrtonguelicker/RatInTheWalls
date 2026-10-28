import random
import sys

class Player: 
    
    """ Player class of the game

    Player has: 
        name - string: player's chosen name
        health - integer: current health 
        max_health - integer: max health
        attack - integer: atk power
        defense - integer: def value 
        inventory - list: all the items the player is carrying
        current_room: room that the player is in
    """
    
    def __init__(self, name): 
        # create a new player, with just it's name; everything else is auto defaulted to base values
        
        self.name = name 
        self.health = 100 
        self.max_health = 100 
        self.atk = 10 
        self.defense = 5
        self.inventory = []
        self.current_room = None

    def is_alive(self): 
        # self explanatory, checks if player is alive

        return self.health > 0

    def take_damage(self, amount): 
        # reduce player hp by a given amount

        self.health = max(0, self.health - amount)

        if not self.is_alive():
            print(f"\nUh-oh, {self.name} has fallen...")

    def heal(self, amount): 
        # self explanatory, heal the player by a a given amount

        self.health = min(self.max_health, self.max_health + amount)

        print(f"{self.name} has healed for {amount} HP. ({self.health}/{self.max_health})")

    def add_item(self, item): 
        # append item to player's inventory (list)
        
        self.inventory.append(item)
        
        print(f"Picked up: {item}")
    
    def show_inventory(self): 
        # display current inventory
        
        if not self.inventory: 
            print ("Get a job, you got nothing right now.") ##Change before merging into main
        else: 
            print ("Inventory: ")
            ## add a loop to iterate over inventory list

    def __str__(self): 
        # return what the player is

        return f"{self.name} - HP: {self.health}/{self.max_health}"

    
def parse_command(input): 
    # action = first word, everything else is what the action should be directed towards
    words = input.strip().lower().split()

    if not words: 
        return(None, None)

    action = words[0]
    target = " " 

    # takes "words", and joins everything except the first word in a string called "target"
    if len(words) > 1: 
        target.join(words[1:])
    else: 
        target = None
    
    return (action, target)

def game_loop(): 
    # main game loop

    print ("\nType 'help' for a list of commands.\n")

    help = '''
                go <direction> - Move north/south/east/west
                look           - Look around the room 
                inventory      - Check your inventory 
                take <item>    - Pick up item 
                attack         - Attack an enemy in the room (cruel)
                heal           - Use a HP potion
                quit           - Exit game
           ''' 
    while player.is_alive():
        ## TODO: print current room description and handle player inputs
        return 

def main():
    # start of the game and get player name

    name = input ("Enter your name, adventurer: ")
    if not name: 
        name = "Adventurer"
    name_stripped = name.strip()

    player = Player(name_stripped)
    print(f"\nWelcome, {player.name}. You feel the walls watching you...")

    # start game loop 
    # game_loop(player)
     
    return