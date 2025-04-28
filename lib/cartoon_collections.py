def roll_call_dwarves(list):
    #pass
    for index, dwarve in enumerate(list):
        print(f"{index + 1}. {dwarve}")

def summon_captain_planet(list):
    #pass
    return [char.capitalize() + "!" for char in list]

def long_planeteer_calls(list):
    #pass
    for word in list:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(list):
    #pass
    target_cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in list:
        if cheese in target_cheeses:
            return cheese
