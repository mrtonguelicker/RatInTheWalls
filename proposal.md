# COMP 1110 Project Proposal

## Rat in the Walls

**Team Members:** Pragyay, Imim, Francheska, Marce

**Github Repository:** https://github.com/mrtonguelicker/RatInTheWalls

--- 

### Description

RatInTheWalls is a text-based dungeon crawler which lives and runs entirely in the Terminal (no GUI), along with ocassional ASCII art for important moments and items. The player navigates through a series of connected rooms, encounters enemies, collects items and engages in comant (turn-based). 

### Inputs 

These are the inupts that the will be dewsigned to handle and process (final product may vary slightly).

- Player name (String – entered at the start of the game)
- Commands typed by the player: Movement inputs ('go north', 'go shouth', etc.), actions ('look', 'take item', 'inventory', 'attack', 'heal') and system commands ('help', 'quit')

### Outputs 

- Room descriptions and available exits from the current room printed in the terminal. 
- ASCII art on some if not all enemy visual encouters. 
- Combat status update (damage dealt, damage taken, health bars)
- Inventory lists
- Win/loss messages

### Planned functions and classes 

| File | Owner | Classes/Functions | 
|------|-------|-------------------|
| main | Pragyay | Player class, parse_command(), game_loop(), main() |
| combat | Pragyay | Combat (player, enemy_type), combat loop, calculating damage |
| rooms | Imim | Room class (descriptions, connectios, items, enemies), room creation and links |
| items | Marce | Item class (name, type, what it does), item creations, item function, healing and weapon logic |
| enemies | Francheska | Enemy class (name, health, attack, defense, ASCII art), similar to Player class
| test_game | Shared | pytests for Player, Room, Item, Enemy, combat and command parsing |
| | | |

### Branching Summary

All individual work will be done in designated branches to keep track of who did what and to have a safe copy of a working version at all times.

Branches will be merged with main after at least 3 people approve the PR.