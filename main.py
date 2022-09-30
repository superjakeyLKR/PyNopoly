import os

from random import randint, choice as randchoice

from dataclasses import dataclass, field, asdict
from typing import List

from json import load, dump


def Title():
    print("             "+"#" * 72,end="") 
    print("""
                ##      ## ######## ##        ######   #######  ##     ## ######## 
                ##  ##  ## ##       ##       ##    ## ##     ## ###   ### ##             
                ##  ##  ## ##       ##       ##       ##     ## #### #### ##             
                ##  ##  ## ######   ##       ##       ##     ## ## ### ## ######         
                ##  ##  ## ##       ##       ##       ##     ## ##     ## ##             
                ##  ##  ## ##       ##       ##    ## ##     ## ##     ## ##             
                 ###  ###  ######## ########  ######   #######  ##     ## ########""")
    print("""
                                    ########  #######  
                                       ##    ##     ## 
                                       ##    ##     ## 
                                       ##    ##     ## 
                                       ##    ##     ## 
                                       ##    ##     ## 
                                       ##     #######""")
    print("""
             ########  ##    ## ##    ##  #######  ########   #######  ##       ##    ## 
             ##     ##  ##  ##  ###   ## ##     ## ##     ## ##     ## ##        ##  ##  
             ##     ##   ####   ####  ## ##     ## ##     ## ##     ## ##         ####   
             ########     ##    ## ## ## ##     ## ########  ##     ## ##          ##    
             ##           ##    ##  #### ##     ## ##        ##     ## ##          ##    
             ##           ##    ##   ### ##     ## ##        ##     ## ##          ##    
             ##           ##    ##    ##  #######  ##         #######  ########    ##""")
    print("             "+"#" * 72)

def SettingsTitle():
    print("*" * 72,end="")
    print("""  
 ######  ######## ######## ######## #### ##    ##  ######    ######  
##    ## ##          ##       ##     ##  ###   ## ##    ##  ##    ## 
##       ##          ##       ##     ##  ####  ## ##        ##       
 ######  ######      ##       ##     ##  ## ## ## ##   ####  ######  
      ## ##          ##       ##     ##  ##  #### ##    ##        ## 
##    ## ##          ##       ##     ##  ##   ### ##    ##  ##    ## 
 ######  ########    ##       ##    #### ##    ##  ######    ######""")
    print("*" * 72)

def ClearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def SaveSettings(money, double_land_on_go, cant_buy_on_first_turn, tax_goes_in_middle):
    with open("settings.json", "w") as f:
        dump({"starting_money": money, 
        "double_land_on_go": double_land_on_go, 
        "cant_buy_on_first_turn": cant_buy_on_first_turn, 
        "tax_goes_in_middle": tax_goes_in_middle}, f)


@dataclass
class Property:
    name: str
    cost: int
    #houses: int = 0 #five is a hotel
    rent: List[int] = field(default=List[int])
    owner: str = None

@dataclass
class Railroad(Property):
    houses = 0

@dataclass
class Utility(Property):
    houses = 0

@dataclass
class Card:
    name: str
    gain: int

@dataclass
class CardGiver:
    name: str

@dataclass
class Tax:
    name: str
    amount: int

@dataclass
class Misc:
    name: str

@dataclass
class Player:
    name: str
    money: int
    turns_in_jail = 0
    position = 0
    landed_on_go = False
    passed_go = False

cards = [
    Card("Bank pays you dividend of $50", 50),
    Card("Bank error in your favor, collect $200", 200),
    Card("Advance to Go (Collect $200)", 200),
    Card("You have won second prize in a beauty contest, collect $10", 10),
    Card("You inherit $100", 100),
    Card("From sale of stock you get $50", 50),
    Card("Late fees for medical bills, pay $15", -15),
    Card("Pay hospital fees of $100", -100),
    Card("Pay school fees of $150", -150),
    Card("You have won first prize in a beauty contest, collect $50", 50),
    Card("Water bill, pay $25", -25),
    Card("Pay parking fine of $60", -60),
]

board = [
    Misc("Go"),
    Property("Mediterranean Avenue", 60, [2, 10, 30, 90, 160, 250]),
    CardGiver("Community Chest"),
    Property("Baltic Avenue", 60, [4, 20, 60, 180, 320, 450]),
    Tax("Income Tax", 200),
    Railroad("Reading Railroad", 200),
    Property("Oriental Avenue", 100, [6, 30, 90, 270, 400, 550]),
    CardGiver("Chance"),
    Property("Vermont Avenue", 100, [6, 30, 90, 270, 400, 550]),
    Property("Connecticut Avenue", 120, [8, 40, 100, 300, 450, 600]),
    Misc("Just Visiting"),
    Property("St. Charles Place", 140, [10, 50, 150, 450, 625, 750]),
    CardGiver("Community Chest"),
    Property("States Avenue", 140, [10, 50, 150, 450, 625, 750]),
    Property("Virginia Avenue", 160, [12, 60, 180, 500, 700, 900]),
    Railroad("Pennsylvania Railroad", 200),
    Property("St. James Place", 180, [14, 70, 200, 550, 750, 950]),
    CardGiver("Chance"),
    Property("Tennessee Avenue", 180, [14, 70, 200, 550, 750, 950]),
    Property("New York Avenue", 200, [16, 80, 220, 600, 800, 1000]),
    Misc("Free Parking"),
    Property("Kentucky Avenue", 220, [18, 90, 250, 700, 875, 1050]),
    CardGiver("Community Chest"),
    Property("Indiana Avenue", 220, [18, 90, 250, 700, 875, 1050]),
    Property("Illinois Avenue", 240, [20, 100, 300, 750, 925, 1100]),
    Railroad("B. & O. Railroad", 200),
    Property("Atlantic Avenue", 260, [22, 110, 330, 800, 975, 1150]),
    Property("Ventnor Avenue", 260, [22, 110, 330, 800, 975, 1150]),
    CardGiver("Chance"),
    Property("Marvin Gardens", 280, [24, 120, 360, 850, 1025, 1200]),
    Misc("Go To Jail"),
    Property("Pacific Avenue", 300, [26, 130, 390, 900, 1100, 1275]),
    Property("North Carolina Avenue", 300, [26, 130, 390, 900, 1100, 1275]),
    CardGiver("Chance"),
    Property("Pennsylvania Avenue", 320, [28, 150, 450, 1000, 1200, 1400]),
    Railroad("Short Line", 200),
    CardGiver("Community Chest"),
    Property("Park Place", 350, [35, 175, 500, 1100, 1300, 1500]),
    Tax("Luxury Tax", 100),
    Property("Boardwalk", 400, [50, 200, 600, 1400, 1700, 2000]),
]

def main():
    try:
        #load it if settings.json exists and has data
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                settings = load(f)
                money = settings["starting_money"]
                double_land_on_go = settings["double_land_on_go"]
                cant_buy_on_first_turn = settings["cant_buy_on_first_turn"]
                tax_goes_in_middle = settings["tax_goes_in_middle"]
        else:
            money = 1500
            double_land_on_go, cant_buy_on_first_turn, tax_goes_in_middle = False, False, False    

        Title()
        #ask for player names
        #ask for number of players
        #create players

        option = input("What would you like to do?\n1. Play\n2. Load Game\n3. Open Settings\n")
        ClearScreen()
        if option == "1":
            player_num = int(input("How many players? "))

            while player_num < 2 or player_num > 6:
                print("Invalid number of players")
                player_num = int(input("How many players? "))

            players = []

            for i in range(player_num):
                name = input("Player {}'s Name: ".format(i+1))
                players.append(Player(name, money))

            ClearScreen()

        elif option == "2":
            print("Not implemented yet")
            print("Probably not gonna happen")
            input("Press enter to continue")
            ClearScreen()
            main()
        elif option == "3":
            SettingsTitle()
            option = input("What would you like to do?\n1. Change starting money\n2. Add house rules\n3. Back\n")
            ClearScreen()
            SettingsTitle()
            if option == "1":
                print(f"Current starting money: {money}")
                money = int(input("What would you like to change it to?\n"))
                print(f"Starting money changed to {money}")

                input("Press enter to continue")
            elif option == "2":
                print("Current settings:")
                print(f"Double land on go: {double_land_on_go}")
                print(f"Cant buy on first turn: {cant_buy_on_first_turn}")
                print(f"Tax goes in middle: {tax_goes_in_middle}")
                option = input("What would you like to do?\n1. Change double land on go\n2. Change can't buy on first turn\n3. Change tax goes in middle\n4. Back\n")
                
                if option == "1":
                    double_land_on_go = not double_land_on_go
                    print(f"Double land on go changed to {double_land_on_go}")
                    input("Press enter to continue")

                elif option == "2":
                    cant_buy_on_first_turn = not cant_buy_on_first_turn
                    print(f"Cant buy on first turn changed to {cant_buy_on_first_turn}")
                    input("Press enter to continue")

                elif option == "3":
                    tax_goes_in_middle = not tax_goes_in_middle
                    print(f"Tax goes in middle changed to {tax_goes_in_middle}")
                    input("Press enter to continue")

                else:
                    print("Invalid option")
                    input("Press enter to continue")

            SaveSettings(money, double_land_on_go, cant_buy_on_first_turn, tax_goes_in_middle)
            ClearScreen()
            main()
        else:
            print(f"{option} is an invalid option")
            input("Press enter to continue")
            ClearScreen()
            main()

        if tax_goes_in_middle: middle = 0
        else: middle = -1

        while 1:
            for player in players:
                turns = 0
                roll, roll2 = 0, 0
                #makes sure that the player still to roll
                #if they get a double they get another chance
                while roll == roll2:
                    print(f"\n{player.name}'s turn")

                    if turns > 0: print(f"Double number {turns}")
                    turns += 1
                    if turns == 4: #Actually the third turn
                        print("You have rolled a double 3 times in a row. You are now in jail")
                        player.in_jail = True
                        player.turns_in_jail = 3
                        player.location = 10
                        input("Press enter to continue")
                        break
                    if player.turns_in_jail > 0:
                        print(f"{player.name} is in jail")
                        print(f"{player.name} has {player.turns_in_jail} turns left in jail")
                        print(f"{player.name} has {player.money} dollars")
                        choice = input("What would you like to do?\n1. Roll\n2. Pay $50\n")

                        if choice in ["1", "roll", "r"]:
                            roll, roll2 = randint(1, 6), randint(1, 6)
                            print(f"{player.name} rolled a {roll} and a {roll2}.")

                            if roll == roll2:
                                player.turns_in_jail = 0
                                print("They are now out of jail.")
                            else:
                                player.turns_in_jail -= 1
                                print(f"{player.name} has {player.turns_in_jail} turns left in jail")
                                if player.turns_in_jail == 0:
                                    print(f"{player.name} is now out of jail.")

                        elif choice in ["2", "pay", "p"]:
                            player.money -= 50
                            print(f"{player.name} paid $50")
                            player.turns_in_jail = 0
                            print(f"{player.name} is now out of jail.")

                        else:
                            print("Invalid option")
                            input("Press enter to continue")
                            ClearScreen()
                            continue
                    else:
                        not_roll = True
                        print(f"Money: ${player.money}")
                        while not_roll:
                            choice = input("What would you like to do?\n1. Roll to move\n2. Information\n")
                            if choice in ["1", "roll", "r"]:
                                not_roll = False
                                ClearScreen()
                                roll, roll2 = randint(1, 6), randint(1, 6)
                                print(f"{player.name} rolled a {roll} and a {roll2}.")
                                player.position += (roll + roll2)
                                if player.position > 39:
                                    player.position -= 40
                                    print(f"{player.name} passed go and collected $200")
                                    player.money += 200
                                    player.passed_go = True
                                print(f"{player.name} is on {board[player.position].name}")
                                if issubclass(board[player.position].__class__, Property):
                                    _property = board[player.position]

                                    if _property.owner is None:
                                        if cant_buy_on_first_turn and not player.passed_go:
                                            print(f"{player.name} cannot buy this property")
                                            input("Press enter to continue")
                                            ClearScreen()
                                            continue

                                        else:
                                            print(f"It costs ${_property.cost}")
                                            choice = input("What would you like to do?\n1. Buy\n2. Pass\n")

                                            if choice in ["1", "buy", "b"]:
                                                if player.money >= _property.cost:
                                                    player.money -= _property.cost
                                                    _property.owner = player.name
                                                    print(f"{player.name} bought {_property.name} for ${_property.cost}")
                                                    input("Press enter to continue")
                                                    ClearScreen()
                                                    continue

                                                else:
                                                    print(f"{player.name} cannot afford {_property.name}")
                                                    input("Press enter to continue")
                                                    ClearScreen()
                                                    continue

                                            elif choice in ["2", "pass", "p"]:
                                                print(f"{player.name} passed on {_property.name}")
                                                input("Press enter to continue")
                                                ClearScreen()
                                                continue
                                            else:
                                                print("Invalid option")
                                                input("Press enter to continue")
                                                ClearScreen()
                                                continue
                                    else:
                                        #find the owner from the list of players
                                        for _player in players:
                                            if _player.name == _property.owner:
                                                owner = _player
                                                break
                                        
                                        if owner.name == player.name:
                                            print(f"{player.name} owns {_property.name}")
                                            input("Press enter to continue")
                                            ClearScreen()
                                            continue

                                        print(f"{player.name} is paying rent to {owner.name}")
                                        if player.money >= _property.rent[0]:
                                            owner.money += _property.rent[0]
                                            player.money -= _property.rent[0]
                                            print(f"{player.name} paid ${_property.rent[0]} to {owner.name}")
                                        else:
                                            print(f"{player.name} cannot afford to pay the full rent.")

                                        input("Press enter to continue")
                                        ClearScreen()
                                        continue
                                elif issubclass(board[player.position].__class__, Tax):
                                    player.money -= board[player.position].amount
                                    print(f"{player.name} paid ${board[player.position].amount} in taxes")
                                    if middle > 0: 
                                        middle += board[player.position].amount
                                        print("It was put into the middle!")
                                    input("Press enter to continue")
                                    ClearScreen()
                                    continue
                                elif issubclass(board[player.position].__class__, CardGiver):
                                    card = randchoice(cards)
                                    left_bar = " " * (len(card.name) + 2) + "|" 
                                    print("|" + "-" * (len(card.name) + 2) + "|")
                                    print(f"|{left_bar}\n| {card.name} |\n|{left_bar}")
                                    print("|" + "-" * (len(card.name) + 2) + "|")
                                    input("Press enter to continue")
                                    player.money += card.gain
                                    ClearScreen()
                                    continue
                                elif issubclass(board[player.position].__class__, Misc):
                                    print(board[player.position].name)
                                    if board[player.position].name == "Go to Jail":
                                        player.position = 10
                                        print(f"{player.name} went to jail")
                                        input("Press enter to continue")
                                        ClearScreen()
                                        continue
                                    elif board[player.position].name == "Just Visiting":
                                        #find the players who are in jail
                                        in_jail = []

                                        for _player in players:
                                            if _player.turns_in_jail > 0:
                                                in_jail.append(_player)

                                        print(f"{player.name} was just visiting: ")

                                        if len(in_jail) == 0:
                                            print("Nobody!")
                                        else:
                                            for _player in in_jail:
                                                print(_player.name)

                                    elif board[player.position].name == "Free Parking":
                                        if middle > 0:
                                            print(f"{player.name} collected ${middle} from the middle")
                                            middle = 0
                                        else:
                                            print(f"{player.name} gets to park free, I guess")
                                    
                                    elif board[player.position].name == "Go" and double_land_on_go:
                                        player.money += 400
                                        print(f"{player.name} got $400 for landing on Go")

                                    input("Press enter to continue")
                                    ClearScreen()
                                    continue
                                else: print("HOW DID YOU GET HERE?")
                            elif choice in ["2", "info", "i", "information"]:
                                ClearScreen()
                                print(f"You are on {board[player.position].name}")
                                print(f"You own: ")
                                i=0
                                for _property in board:
                                    if issubclass(_property.__class__, Property) and _property.owner == player.name:
                                        print(_property.name)
                                        i+=1
                                if i==0:
                                    print("No properties. (Yet!)")
                                    if middle > 0:
                                        print(f"There is ${middle} in the middle. (You can take it if you land on Free Parking!)")
                                input("Press enter to continue")
                                ClearScreen()
                                continue
                        else:
                            continue
    except KeyboardInterrupt:
        print("Exiting the game...")
        input("Press enter to continue")
    except:
        print("An error has occured. Please contact the developer. Exiting program...")
        input("Press enter to continue")

if __name__ == "__main__":
    main()