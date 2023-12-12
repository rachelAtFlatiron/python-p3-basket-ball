def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

# def get_player(name):
#     home_player = [player for player in game_dict()['home']['players'] if player['name'] == name]
#     away_player = [player for player in game_dict()['away']['players'] if player['name'] == name]
#     return home_player[0] if len(home_player) > 0 else away_player[0]

def all_players():
    all_players = {}
    dict = game_dict()
    for key in dict: #get the current team
        #key will be either 'home' or 'away'
        cur_team = dict[key]
        all_cur_team_players = cur_team['players']
        for player in all_cur_team_players: #loop through current team's players
            #player['name'] for the key (ex. "jarrett allen") and player for value(the entire object)
            all_players[player['name']] = player 
    return all_players

def get_player(name):
    return all_players()[name]
    
def get_team(name):
    dict = game_dict()
    for key in dict: #'home' or 'away'
        if dict[key]['team_name'] == name:
            return dict[key] #the entire object
    return None 

def num_points_per_game(name):
    return get_player(name)["points_per_game"]

def player_age(name):
    return get_player(name)["age"]

def team_colors(team_name):
    return get_team(team_name)['colors']

#when you are iterating over an object, you are iterating over the keys
# for team in dict
# 1. home
# 2. away 
# 3. ....
def team_names():
    # [return for element in array if conditional]
    dict = game_dict()
    return [
    #what we want to return: team['team_name']
        dict[key]['team_name'] for 
    #what we are looping over: loop over each key in object
        key 
        in dict
    ]
    #[dict[key]['team_name'] for key in dict]

def player_numbers(team_name):
    team_players = get_team(team_name)['players']
    #[return for el in iterator]
    #return player['number'] 
    #player 
    #team_players
    return[player['number'] for player in team_players]
    #in JS: team_players.map(player => player['number'])


def player_stats(name):
    return get_player(name)

def average_rebounds_by_shoe_brand():
    shoes = {}
    players = all_players()
    #iterate over players 
    for player_name in players: #player_name is only the key
        try:
            cur_player = players[player_name]
            #for player's rebounds
            rebounds = cur_player['rebounds_per_game']
            #append to shoes[brand]
            shoes[cur_player['shoe_brand']].append(rebounds)
        except KeyError:
            shoes[cur_player['shoe_brand']] = [cur_player['rebounds_per_game']]
    #sum, average
    for shoe_brand in shoes: #shoe_brand is only the key
        rebounds = shoes[shoe_brand]
        avg = sum(rebounds)/len(rebounds)
        # NEEDS DOUBLE SPACE AFTER : FOR THE TEST TO PASS
        print(f'{shoe_brand}:  {"{:.2f}".format(avg)}')
