import random 

# Yeah this terrifying but I'm already a demon.
firstNames = [
    "Amber", "Armored", "Ashen", "Assassin", "Bastard", "Biting", "Bitter", "Black", 
    "Blazing", "Bloody", "Blue", "Brass", "Brutal", "Bullet", "Cannibal", "Charging", 
    "Code", "Copper", "Crawling", "Creeping", "Crimson", "Crying", "Crystal", "Cunning", 
    "Dancing", "Dark", "Death", "Devil", "Dire", "Dizzy", "Doom", "Emerald", "Fire", 
    "Flaming", "Frantic", "Frigid", "Garnet", "Glacier", "Goblin", "Golden", "Gray", 
    "Greedy", "Green", "Grizzly", "Growling", "Hinting", "Hissing", "Howling", "Hulking", 
    "Hungry", "Hunting", "Ice", "Iron", "Ivory", "Jade", "Jumping", "Killer", "Laughing", 
    "Lonely", "Mad", "Midnight", "Night", "Obsidian", "Ochre", "Onyx", "Panzer", "Pirate", 
    "Poison", "Pouncing", "Prowling", "Punching", "Rabid", "Raging", "Rampant", "Rancid", 
    "Raving", "Razor", "Roaring", "Rogue", "Rumble", "Running", "Sadistic", "Scowling", 
    "Seething", "Shining", "Silent", "Sinister", "Sky", "Sly", "Smiling", "Smoking", 
    "Spitting", "Spunky", "Spying", "Stalking", "Steel", "Stiker", "Stone", "Striker", 
    "Stubborn", "Sunny", "Thunder", "Titanium", "Tree", "Twilight", "Vampire", "Vengeful", 
    "Vile", "Viridian", "White", "Wild", "Ziang"
]

lastNames = [
    "Adder", "Agama", "Armadillo", "Badger", "Barracuda", "Basilisk", "Bat", "Bear", 
    "Beetle", "Bidon", "Bison", "Boa", "Boar", "Buffalo", "Bull", "Buzzard", 
    "Canine", "Capybara", "Cat", "Centipede", "Chameleon", "Cheetah", "Cobra", 
    "Coyote", "Crab", "Crocodile", "Crow", "Dhole", "Dingo", "Dragon", "Eagle", 
    "Echidna", "Eel", "Elephant", "Elk", "Falcon", "Frog", "Gator", "Gecko", 
    "Gibbon", "Goat", "Gopher", "Griffon", "Harrier", "Hawk", "Hedgehog", "Heron", 
    "Hippo", "Hog", "Hornet", "Hound", "Husky", "Hyena", "Iguana", "Jackal", 
    "Jaguar", "Kangaroo", "Koala", "Komodo", "Leopard", "Lion", "Lizard", "Llama", 
    "Lynx", "Macaw", "Malak", "Mammoth", "Mantis", "Marlin", "Marmot", "Mastiff", 
    "Mastodon", "Mole", "Mongoose", "Moose", "Mosquito", "Moth", "Mouse", "Mustang", 
    "Octopus", "Orca", "Osprey", "Ostrich", "Otter", "Owl", "Ox", "Panda", "Panther", 
    "Parrot", "Phoenix", "Piranha", "Platypus", "Python", "Raccoon", "Ram", "Raptor", 
    "Rat", "Raven", "Ray", "Rhino", "Roach", "Rooster", "Salamander", "Salamander", 
    "Serpent", "Shark", "Sloth", "Slug", "Sparrow", "Spider", "Squirrel", "Stallion", 
    "Sturgeon", "Swan", "Talker", "Tan", "Tarantual", "Tarantula", "Tiger", "Tigress", 
    "Tree frog", "Turkey", "Viper", "Vulture", "Wallaby", "Wasp", "Weasel", "Weevil", 
    "Whale", "Wolf", "Wombat", "Worm", "Zebra"
]

# The program running. 
while True:
    generatedName = ""
    randomFirstName = random.choice(firstNames)
    randomLastName = random.choice(lastNames)

    generatedName += randomFirstName + " " + randomLastName             

    print("Welcome to Diamond Dogs:", generatedName + "!") 
    
    userChoice = input("Do you want to generate a new name? (Type & press any key for yes n for no): ")

    if userChoice.lower() == "n":
        print("You're a true diamond", generatedName + ".")
        break
