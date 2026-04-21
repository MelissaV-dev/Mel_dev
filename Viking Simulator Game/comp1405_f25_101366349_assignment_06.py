# Name Melissa Vaziri
# Student ID 101366349
# Date: 11/28/2025
import sys
import random
import updated_base_module_for_101366349 as index


# First Function For Splash Screen Window, And Detailed Border
def window_and_border():
    # Opening the window for "North European Kingdoms"
    index.open_surf("North European Kingdom")
    # Filling The Screen To "Sea"
    index.fill_surf(18, 83, 89)
    # This is to draw the big rectangle
    index.draw_rect((120, 150, 400, 100), (255, 0, 0), 200)
    index.draw_line((150, 160), (490, 160), (255, 255, 255), 3)  # Massive horizontal white line (top)
    index.draw_line((150, 240), (490, 240), (255, 255, 255), 3)  # Massive horizontal white line (bottom)
    index.draw_line((135, 175), (135, 225), (255, 255, 255), 3)  # The left side white line
    index.draw_line((505, 175), (505, 225), (255, 255, 255), 3)  # The right side white line
    # left connector of top white line and left side line
    index.draw_line((150, 160), (150, 165), (255, 255, 255), 3)  # small down line with a length of 5
    index.draw_line((150, 165), (140, 165), (255, 255, 255), 3)  # To the left with a length of 10
    index.draw_line((140, 165), (140, 175), (255, 255, 255), 3)  # Same length as above, but down
    index.draw_line((140, 175), (135, 175), (255, 255, 255), 3)  # Small to the left with a length of 5
    # right connector of top white line and right side line
    index.draw_line((490, 160), (490, 165), (255, 255, 255), 3)  # Small down
    index.draw_line((490, 165), (500, 165), (255, 255, 255), 3)  # To the right
    index.draw_line((500, 165), (500, 175), (255, 255, 255), 3)  # Same length as above, down
    index.draw_line((500, 175), (505, 175), (255, 255, 255), 3)  # Small to the right
    # left connector of bottom white line and left side line
    index.draw_line((135, 225), (140, 225), (255, 255, 255), 3)  # small to the right
    index.draw_line((140, 225), (140, 235), (255, 255, 255), 3)  # down
    index.draw_line((140, 235), (150, 235), (255, 255, 255), 3)  # Same length as above, but to the right
    index.draw_line((150, 235), (150, 240), (255, 255, 255), 3)  # Small down
    # right connector of bottom white line and right side line
    index.draw_line((505, 225), (500, 225), (255, 255, 255), 3)  # Small left
    index.draw_line((500, 225), (500, 235), (255, 255, 255), 3)  # Down
    index.draw_line((500, 235), (490, 235), (255, 255, 255), 3)  # Same length as above, but to the left
    index.draw_line((490, 235), (490, 240), (255, 255, 255), 3)  # Small down
    # tiny square top-left
    index.draw_line((145, 165), (145, 160), (255, 255, 255), 3)  # Small up (by 5)
    index.draw_line((145, 160), (135, 160), (255, 255, 255),
                    3)  # Going to x-position on the left side line, horizontal (ends up being 10)
    index.draw_line((135, 160), (135, 170), (255, 255, 255), 3)  # Going down 10
    index.draw_line((135, 170), (140, 170), (255, 255, 255), 3)  # Going right 5
    # tiny square top-right
    index.draw_line((495, 165), (495, 160), (255, 255, 255), 3)  # Small up (by 5)
    index.draw_line((495, 160), (505, 160), (255, 255, 255),
                    3)  # Going to the x-position right side line, horizontal (ends up being 10)
    index.draw_line((505, 160), (505, 170), (255, 255, 255), 3)  # Go down 10
    index.draw_line((505, 170), (500, 170), (255, 255, 255), 3)  # Go left 5
    # tiny square bottom-left
    index.draw_line((140, 230), (135, 230), (255, 255, 255), 3)  # Go to x-position left-side line (small 5)
    index.draw_line((135, 230), (135, 240), (255, 255, 255), 3)  # Go down 10
    index.draw_line((135, 240), (145, 240), (255, 255, 255), 3)  # Go right 10
    index.draw_line((145, 240), (145, 235), (255, 255, 255), 3)  # Small up
    # tiny square bottom-right
    index.draw_line((500, 230), (505, 230), (255, 255, 255), 3)  # Go to x-position right-side line (small 5)
    index.draw_line((505, 230), (505, 240), (255, 255, 255), 3)  # Going down 10
    index.draw_line((505, 240), (495, 240), (255, 255, 255), 3)  # Going left 10
    index.draw_line((495, 240), (495, 235), (255, 255, 255), 3)  # Small up


# This Is This Second Function To Render The Text
def title_screen():
    # Making The Text White + Implementing The Text
    index.draw_text(180, (255, 255, 255), "Viking Simulator")
    # This Command Basically Holds The Window For A Certain Amount Of Time (5 sec)
    index.hold_surf(50)


# This Third Function displays the title and introduction of the game, and takes one argument as a string, which is the game title
def game_title_and_introduction(viking_simulator):
    game_title = viking_simulator  # Defined game_title for print statement
    # Printing The Game Title
    print(f"Welcome To {game_title}!")
    print("Welcome, travaler, to the lands of the North European Kingdoms ")
    # Inserting an If-Branch Statement Which Asks The Player If They Would Like To Know More About The Objective Of The Game
    player = input("Would You Like To Learn About Your Heroic Mission (Y/N): ")
    if player.lower() == "y":
        # Printing The Objective Of The Game
        print(
            "The objective of this heroic mission is to educate players about feudal systems by guiding a knight on a journey through castles, towns, villages, and lands of the North European Kingdom. Players must make strategic decisions regarding supplies, navigation, and survival, as poor choices can lead to hunger, illness, or accidents along the way.")
    else:
        print("See You Next Time!")


# Function to select random questions from a large collection
def select_random_questions(questions, num_questions):
    # This function randomly selects a subset of questions from a larger collection.
    return random.sample(questions, k=num_questions)


# Function to present the options to the player and check whether a response is correct or not
def ask_question(question_data):
    # Display the question
    print("\nQUIZ QUESTION:")
    print(question_data["question"])

    # Shuffle the options
    options = question_data["options"].copy()
    random.shuffle(options)  # shuffle options

    # Display the options
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    # Take input from the player
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                break
            else:
                print(f"Please choose a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input! Enter a number.")

    # Check if the answer is correct
    if options[choice - 1] == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was: {question_data['answer']}")
        return False


def run_quiz():
    # Example of a larger collection of questions
    questions = [
        {
            "question": "What is the primary role of a knight?",
            "options": ["To farm crops", "To protect the kingdom", "To hunt animals", "To craft tools"],
            "answer": "To protect the kingdom"
        },
        {
            "question": "Which valley is peaceful and filled with love and community?",
            "options": ["Swalley Valley", "Grey Spike Valley", "Hallow Valley"],
            "answer": "Hallow Valley"
        },
        {
            "question": "What is essential for a hunter's survival?",
            "options": ["Food, resources, and protection", "Gold and jewels", "Clothing sets", "Building castles"],
            "answer": "Food, resources, and protection"
        },
    ]

    # Select 2 random questions for this quiz session
    quiz_questions = select_random_questions(questions, 2)

    score = 0
    for q in quiz_questions:
        if ask_question(q):
            score += 1

    print(f"\nYour quiz score: {score}/{len(quiz_questions)}")


# This while loop is formed for character classes, but also indicates with numbers that are specified to each of the roles, and provides two options within that class
# The user is allowed to pick between that class, and whichever one of the options they pick, it will generate an automatic message by greeting the user
# The code checks the user's input to see if the input is valid or not, and would make them restart the process if the input is not valid
def character_class_selection():
    amount = 101355349
    character_class = 0
    while True:
        try:
            character_class = int(input(
                "Which Character Class Would You Like To Be A Part Of (1.Knight, 2. Craftsman, 3. Farmer, 4. Hunter, 5. Noble)? "))
        except ValueError:
            print("Invalid input. Enter again.")
            continue  # Restart loop if input isn't an integer
        if 0 < character_class < 6:
            if character_class == 1:
                # Displaying Class Descriptions
                print(
                    "The primary role of a knight is to protect the lord, the kingdom, and its citizens by fighting enemies from other realms, serving as bodyguards, maintaining their training and readiness, and remaining loyal to and obedient to the lord's orders.")
                while True:
                    try:
                        character_class = float(
                            input(
                                "Do you want to be part of the Protection Team (1.1) or Combat Team (1.2)? "))
                    except ValueError:
                        print("Invalid input. Enter again.")
                        continue
                    if character_class == 1.1 or character_class == 1.2:
                        if character_class == 1.1:
                            print("Thank you for being part of the Protection Team.")
                        else:
                            print("Thank you for being part of the Combat Team.")
                        break
                    else:
                        print("Invalid input. Enter again.")
            if character_class == 2:
                print(
                    "The primary role of a craftsman is to design and assemble various tools for specific purposes, ensuring proper equipment for combat, construction, or other tasks. They are also responsible for gathering materials such as wood, metal, gold, and sand.")
                while True:
                    try:
                        character_class = float(
                            input(
                                "Do you want to be part of the Gathering material Team (2.1) or Designing/Assembling Team (2.2)? "))
                    except ValueError:
                        print("Invalid input. Enter again.")
                        continue
                    if character_class == 2.1 or character_class == 2.2:
                        if character_class == 2.1:
                            print("Thank you for being part of Gathering Material Team.")
                        else:
                            print("Thank you for being part of Designing/Assembling Team.")
                        break
                    else:
                        print("Invalid input. Enter again.")
            if character_class == 3:
                print(
                    "The role of a farmer is to grow crops and raise livestock for food and other products. They are responsible for planting, feeding, harvesting, maintaining their equipment, and monitoring their fields and animals to ensure everything remains healthy and productive.")
                while True:
                    try:
                        character_class = float(
                            input("Do you want to be part of the Maintainance Team (3.1) or Production Team (3.2)? "))
                    except ValueError:
                        print("Invalid input. Enter again.")
                        continue
                    if character_class == 3.1 or character_class == 3.2:
                        if character_class == 3.1:
                            print("Thank you for being part of the maintainance Team.")
                        else:
                            print("Thank you for being part of the production Team.")
                        break
                    else:
                        print("Invalid input. Enter again.")
            if character_class == 4:
                print(
                    "A hunter finds and captures animals for food, such as meat, as well as for valuable resources like wool, leather, and fur. Hunters provide essential materials that support their society and help ensure survival. They use various methods to catch their prey, including setting traps or engaging in direct combat. In addition to gathering resources, hunters also protect their communities from wild or dangerous animals and from others who may seek to steal those resources.")
                while True:
                    try:
                        character_class = float(
                            input(
                                "Do you want to be part of the hunting food Team (4.1) or the resources Team (4.2)? "))
                    except ValueError:
                        print("Invalid input. Enter again.")
                        continue
                    if character_class == 4.1 or character_class == 4.2:
                        if character_class == 4.1:
                            print("Thank you for being part of the hunting food Team.")
                        else:
                            print("Thank you for being part of the resources Team.")
                            break
                    else:
                        print("Invalid input. Enter again.")
            if character_class == 5:
                print(
                    "A Noble plays an important role in guiding and organizing individuals, whether sending them on missions, gathering food, fighting for the kingdom, or providing entertainment. Leaders are responsible for making wise decisions, supporting the kingdom's stability, and protecting the well-being of society.")
                while True:
                    try:
                        character_class = float(
                            input("Do you want to be part of the organizing Team (5.1) or desicion Team (5.2)? "))
                    except ValueError:
                        print("Invalid input. Enter again.")
                        continue
                    if character_class == 5.1 or character_class == 5.2:
                        if character_class == 5.1:
                            print("Thank you for being part of the organizing Team.")
                        else:
                            print("Thank you for being part of the descision Team.")
                        break
                    else:
                        print("Invalid input. Enter again.")
            break
        else:
            print("Invalid input. Enter again.")
    # Producing The Two Return Values, One As An Integer Such As The Amount Currency, And Second Integer Is The Character Class
    return amount, character_class


def my_find_function(main_string, sub_string):
    # This function will be replacing the built-in find() method.
    for i in range(len(main_string) - len(sub_string) + 1):
        if main_string[i:i + len(sub_string)] == sub_string:  # using slicing
            return i
    return -1


def find_and_replace(event, name):
    # This function uses the find_and_replace and the slicing/concatenation operators.
    substring = "RANDOM_NAME"
    index_position = my_find_function(event, substring)
    if index_position == -1:
        return event
    # this basically uses slicing to remove paired text, and connects the rest as a whole
    return event[:index_position] + name + event[index_position + len(substring):]


def location_selection():
    # Here I'm Asking, Performing A Print Statement To Ask The User If They Would Like To Learn More About The Game Locations
    player = input("Would You Like To Learn About The Locations In The Game? (y/n): ")
    # The Term Player.Lower() Is Basically A Function For Upper Case And Lowercase Letters, Allowing Them To Do Both
    # If The User Says Yes, Then We Print A statement Asking Which Location They Would Like With Specified Numbers
    if player.lower() == "y":
        print(
            "It Is 1000s. Pick Which Location You Would Like To Go To? (1,2,3) 1. Swalley Valley, 2. Grey Spike Valley, 3. Hallow Valley")
    # If They Do Not Want To, Then It Will Print A Statement To End The Question
    else:
        print("See You Next Time!")
    # This Is A Print Of What The Swalley Valley Is Described As For This Location
    print(
        "Swalley Valley Is A Beautiful Place Filled With Mountains, Deserts, Rainforests, And Animals Who Are Always On The Loose!")
    # This Is A Print Statement For What Grey Spike Valley Is Described As For This Location
    print(
        "Grey Spike Valley Is A Place That Is Grey All The Time, Filled With Chaos and Anger As People Battle One Another For The Empire Castle!")
    # This Is A Print Of What Hallow Valley Is Described As For This Location
    print("Hallow Valley Is A Peaceful Location Filled With Love, Care, Compassion, And Unity From The Community!")
    # Adding return values to satisfy the "2 return values or more" requirement
    return "Location Data", 12345


def format_name_manually(name_string):
    # This function fixes capitalization and uppercase at the start of a word, but also lowercase everywhere else.
    # The algorithm must use ord/chr and not the built-in .upper() or .title() methods.
    name_string = name_string.lower()  # convert all to lowercase
    new_string = ""  # use concatenation
    for i in range(len(name_string)):
        ch = name_string[i]
        # Check if it's the start of the string or comes after a space
        if i == 0 or name_string[i - 1] == " ":
            if ch.isalpha():
                ascii_code = ord(ch)
                if 97 <= ascii_code <= 122:  # between 'a' and 'z'
                    ch = chr(ascii_code - 32)  # convert to uppercase manually
        new_string = new_string + ch  # concatenate each character
    return new_string


# Def Main Is Basically Defining The Function, And Is the Initial Starting Point Of The Code
def main():
    # This is basically running in the debug mode, and it needs the sys import
    debug_mode = len(sys.argv) > 1 and sys.argv[1] == "debug"
    # This basically sets the event probability
    event_result = 400

    if debug_mode:
        # This basically makes the debug mode have a 50% chance
        event_result = 50
        print("||||| RUNNING IN DEBUG MODE |||||")

    # The events list has been moved inside main to eliminate a global variable
    events = [
        "RANDOM_NAME Has Died By A Sword",
        "RANDOM_NAME Has Lost Their Way Back Home.",
        "RANDOM_NAME Is Dying Of Hunger",
        "The player has found a hidden village.",
        "The player found a well.",
        "The player found a horse."
    ]
    # New list for events containing RANDOM_NAME which is for debugging
    random_name_events = [f for f in events if "RANDOM_NAME" in f]

    # Basically Creating Two Linear Collections For Landmarks To Be Visited, And For Distances That Separate Them
    landmarks = ["Lord Almara's Castle", "Raba Township", "Roccio's Village", "Duke's Kingdom", "Barnabus Castle"]
    print("The Player Will Be Traveling To Lord Almara's Castle, Duke's Kingdom, And Barnabus Castle")
    distances = [300, 120, 130, 380, 250]

    # This is basically the map I made with the new landmarks in a multidimensional list and in a dictionary collection
    node_names = [
        "Grey Spike Valley",  # 0
        "Swalley Valley",  # 1
        "Hallow Valley",  # 2
        "Knight's Hill",  # 3
        "Stone Tower",  # 4
        "Old Port",  # 5
        "Stone Bridge",  # 6
        "Ravencliff Tower",  # 7
        "Willow Village",  # 8
        "Hawthorne Castle",  # 9
        "King's Village"  # 10
    ]

    # This is basically a Multidimensional collection based on my map with nodes, and connections to other pairs
    map_connections = [
        [0, [6, 7]],  # Grey Spike Valley connects to Stone Bridge and Ravencliff Tower
        [1, [4, 5]],  # Swalley Valley connects to Stone Tower and Old Port
        [2, [7]],  # Hallow Valley connects to Ravencliff Tower
        [3, [6]],  # Knight's Hill connects to Stone Bridge
        [4, [1, 5]],  # Stone Tower connects to Swalley Valley and Old Port
        [5, [1, 4, 8, 9]],  # Old Port connects to Swalley, Stone Tower, Willow, Hawthorne
        [6, [0, 3, 8, 7]],  # Stone Bridge connects to Grey Spike, Knight's Hill, Willow, Ravencliff
        [7, [0, 2, 6, 10]],  # Ravencliff connects to Grey Spike, Hallow, Stone Bridge, King's Village
        [8, [5, 6, 9]],  # Willow connects to Old Port, Stone Bridge, Hawthorne
        [9, [5, 8, 10]],  # Hawthorne connects to Old Port, Willow, King's Village
        [10, [7, 9]]  # King's Village connects to Ravencliff and Hawthorne
    ]

    # This is a associative collection because the dictionary is mapping a node to the following neighbours
    map_graph = {node: neighbours for node, neighbours in map_connections}

    # This gets the possible nodes the player can go to and prompts them to choose one
    def choose_next_destination(current_node):

        while True:
            neighbours = map_graph[current_node]
            print("\nYou are currently at:", node_names[current_node])
            print("From here, you may travel to:")
            for i, n in enumerate(neighbours, start=1):
                print(f"{i}. {node_names[n]}")
            try:
                choice = int(input("Enter the number of the location you wish to travel to: "))
            except ValueError:
                print("Invalid input. Enter again.")
                continue
            if 1 <= choice <= len(neighbours):
                return neighbours[choice - 1]
            else:
                print("Please choose a valid option.")

    # Calling the splash screen and introduction functions
    window_and_border()
    title_screen()
    game_title_and_introduction("North European Kingdom")

    # this will essentially run a quiz before the departure
    print("\nBefore starting your journey, test your knowledge with a short quiz!")
    run_quiz()

    # Calling character class selection
    amount, character_class = character_class_selection()

    # The Price For The Resources
    tools_unit_price = 100
    wheeled_transport_unit_price = 98
    wood_unit_price = 15
    food_unit_price = 15
    clothing_unit_price = 15

    def departure_date_selection():

        nonlocal wood_unit_price, food_unit_price, clothing_unit_price
        while True:
            try:
                departure_time = int(input(
                    "At What Time Would You Like To Leave? (1,2,3,4,5 ) 1. July, 2. March, 3. December, 4. May, 5. September: "))
            except ValueError:
                print("Invalid input. Enter again.")
                continue
            if 0 < departure_time < 6:
                break
            else:
                print("Invalid input. Enter again.")
        departure_location = 0
        while True:
            try:
                departure_location = int(input(
                    "Which Location Would You Like To Leave? (1,2,3) 1. Swalley Valley, 2. Grey Spike Valley, 3. Hallow Valley: "))
            except ValueError:
                print("Invalid input. Enter again.")
                continue
            if 0 < departure_location < 4:
                break
            else:
                print("Invalid input. Enter again.")
        if departure_location == 1 and departure_time != 1:
            wood_unit_price *= 2
        if departure_location == 2 or departure_time != 2:
            food_unit_price *= 3
        if not departure_location == 3 and departure_time != 3:
            clothing_unit_price *= 5
        return departure_time, departure_location

    def five_party_member_names():

        while True:
            names_in_list = []
            partyleader = input("Enter the name of the party leader: ")
            partyleader = partyleader.strip('!@#$%^&*()')
            partyleader = format_name_manually(partyleader)
            names_in_list.append(partyleader)
            print(names_in_list)
            for x in range(2, 6):
                name = input(f"Enter the name of the team member {x}: ")
                name = name.strip('!@#$%^&*()')
                name = format_name_manually(name)
                names_in_list.append(name)
            user = input("Are The Names Acceptable (Y For Yes / N For No) ")
            if user.lower() == 'n':
                print(f"{names_in_list} Are Not Acceptable")
            else:
                print(f"{names_in_list} are acceptable")
                break
        return names_in_list

    def load_descriptions(filename):
        descriptions = {}

        # open the file manually — no imports needed
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if "=" in line:  # split name and description
                    name, desc = line.split("=", 1)
                    descriptions[name.strip()] = desc.strip()

        return descriptions

    def purchase_single_supply(supply_name, unit_cost, description):

        nonlocal amount, running_total
        print(f"\n--- Purchasing {description} ({supply_name}) ---")
        print(f"I charge ${unit_cost:.2f} dollars Per {supply_name}!")
        try:
            units_purchased = int(input(f"Please enter the amount of {supply_name} you would like to purchase: "))
        except ValueError:
            print("Invalid input. Enter a whole number. 0 units purchased.")
            return 0, 0.0
        item_total = unit_cost * units_purchased
        if amount >= item_total:
            running_total += item_total
            amount -= item_total
            print(f"Purchase successful. Total item cost: ${item_total:.2f}")
            print(f"The running total spent is ${running_total:.2f}, amount remaining : ${amount:.2f}")
            return units_purchased, float(item_total)
        else:
            print("You Do Not Have Enough Money In Your Account. Purchase failed.")
            return 0, 0.0

    # Calling the location and date selection functions (now returning values)
    location_selection()
    departure_time, departure_location = departure_date_selection()

    party = five_party_member_names()
    print(f"The Final Member In The Party, {party}")  # this is to print the display party list properly

    print(
        "Before leaving the stronghold, you should buy equipment and supplies. You have 101366349 in cash but you do not need to spend it all now. ")

    running_total = 0

    revise_choices = "y"
    while revise_choices.lower() == "y":
        units_wood, cost_wood = purchase_single_supply("Log", wood_unit_price, "Wood Supply")
        units_food, cost_food = purchase_single_supply("set of food", food_unit_price, "Food Rations")
        units_clothing, cost_clothing = purchase_single_supply("clothing set", clothing_unit_price, "Clothing Sets")
        units_tool, cost_medical = purchase_single_supply("purchasing tools", tools_unit_price, "tool supplies")
        units_wheeled, cost_transport = purchase_single_supply("Wheeled transport unit", wheeled_transport_unit_price,
                                                               "Wheeled Transportation")
        revise_choices = input("\nWould You Like To Revise Your Purchases, And Restart? (y/n): ")

    index.open_surf("North European Kingdom")
    player_sprite = index.open_sprite("wagon_sprite_for_101366349.png")
    index.set_font_for_small_text("JetBrainsMono-Regular.ttf")

    user_quit = False
    spacing = 20
    road = [n for n in range(0, 680, spacing)]
    curr_node = 0
    description_texts = load_descriptions("descriptions.txt")
    print('here:')
    print(description_texts)

    while True:
        curr_node = choose_next_destination(curr_node)

        if user_quit:
            break
        print(f"The Commencement Of Your Journey To {node_names[curr_node]}.")

        road_line_offset = 0
        distance = 200

        while distance > 0:
            user_quit = index.has_key_been_pressed()
            if user_quit:
                break

            index.fill_surf(29, 43, 83)
            index.draw_rect((0, 250, 680, 150), (29, 43, 83), 0)

            for n in road:
                x = n + road_line_offset
                if x > 680:
                    x -= 680
                index.draw_line((x, 250), (x, 400), (255, 255, 255), 3)

            index.blit_image(player_sprite, 300, 300)
            index.draw_text(20, (255, 255, 255), f"Distance remaining: {distance}")

            if random.randint(1, event_result) == 1:
                if debug_mode:
                    event_message = random.choice(random_name_events)
                else:
                    event_message = random.choice(events)

                if "RANDOM_NAME" in event_message:
                    random_member = random.choice(party[1:])
                    event_message = find_and_replace(event_message, random_member)

                index.draw_text(100, (255, 255, 0), f"Event: {event_message}")
                print(f"The Game Event: {event_message}")
                response = input("Would You Like To Continue Your Journey (y/n): ")
                if response.lower() != "y":
                    print("You have chosen to end your quest early.")
                    user_quit = True
                    break

            road_line_offset = (road_line_offset + 1) % spacing
            distance -= random.randint(1, 5)
            index.display_update()
            index.time_pause(100)

        if distance <= 0:
            index.render_smaller_text(14, (255, 255, 255), (0, 0, 0), 320, 20, 100,description_texts[node_names[curr_node]])
            index.display_update()
            print("Destination Reached!")


# This is basically going to display the references and attribution for the resources I used for this project
print("\nReferences / Attribution:")
print("Generated with the help of ChatGPT, accessed September 1, 2025")
print("Wagon sprite generated using the command-line wagon sprite utility")
print("Original icon reference: game-icons.net - https://game-icons.net/1x2/skoll/mounted-knight.html")

# Name is basically checking if the file is a module or script
# Main is basically is the main script being run
if __name__ == "__main__":
    main()

