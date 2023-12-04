data = open("input.txt")
valid_colors = ["blue", "red", "green"]
id_sum = 0
power_sum = 0

for game in data:
    #Initialize necessary variables
    game_flag = True
    game_id_flag = False
    blue,red,green = [],[],[]

    #Clean inputs for .isnumeric()
    game = game.replace(":", "")

    #Loop through each game
    for set in game.split(";"):
        for colors in set.split(","):
            for x in valid_colors:
                if(x in colors):
                    for item in colors.split(" "):
                        if(item == "Game"):
                            game_id_flag = True #Next number will be game id
                        
                        if(item.isnumeric() and game_id_flag):
                            game_id = int(item) #Get game id number
                            game_id_flag = False
                        elif(item.isnumeric()):
                            if((x == "red" and int(item) > 12) or (x == "green" and int(item) > 13) or (x == "blue" and int(item) > 14)):
                                game_flag = False   #Excludes games that don't meet conditions
                            
                            #Store for power calculation
                            if(x == "blue"):
                                blue.append(int(item))
                            elif(x == "red"):
                                red.append(int(item))
                            elif(x == "green"):
                                green.append(int(item))

    if(game_flag):
        id_sum += game_id
    
    #Max number of cubes shown is minimum required for game to be possible
    power_sum += max(blue) * max(red) * max(green)

print(id_sum)
print(power_sum)