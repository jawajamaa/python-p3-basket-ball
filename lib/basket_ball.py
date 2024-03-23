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

# list_comprehension = [item for item of items if condition]

# first two methods are helper functions that do not pass tests(as they are not tested)
def get_teams():
    return [team for team in game_dict().values()]
    # team_list = []
    # for team in gd().values():
    #     team_list.append(team)

    # return team  

# print(get_teams())

def get_all_players():
    return [player for team in get_teams() for player in team["players"]] 
    # all_players = []
    # for team in get_teams():
    #     for player in team["players"]:
    #         all_players.append(player)

# print(get_all_players())

# Lab methods being tested
def num_points_per_game(name):
    return next(player["points_per_game"] for player in get_all_players() if player["name"] == name)
    # for player in get_all_players():
    #     if player[name] == name:
    #         return player["points_per_game"]

# print(num_points_per_game("Davis Bertans"))

def player_age(name):
    return next(player["age"] for player in get_all_players() if player["name"] == name)

# print(player_age("Davis Bertans"))

def team_colors(team_name):
    # from ChatGPT - Filter teams to find the one with the specified name
    team = next((team for team in get_teams() if team["team_name"] == team_name), None)
    # breakpoint()
    if team:
        return team["colors"]
    else:
        return None

# print(team_colors("Cleveland Cavaliers"))

def team_names():
    teams = [team["team_name"] for team in get_teams()]
    return teams
    # *****************Generator expression returning a generator obj
    # teams = (team["team_name"] for team in get_teams())
    # for team in teams:
    #     return team
    # *************have to iterate through gen obj to access values; return statement 
    # on above line only returns first team as does next()

# print(team_names())

def player_numbers(team_arg):
    return [player["number"] for team in get_teams() for player in team["players"] if team["team_name"] == team_arg]

# print(player_numbers("Washington Wizards"))

def player_stats(player_name):
    return next(player for player in get_all_players()if player["name"] == player_name)

# print(player_stats("Davis Bertans"))

def average_rebounds_by_shoe_brand():
    rebounds_by_shoe = {}
    for player in get_all_players():
        brand = player["shoe_brand"]
        rebounds = player["rebounds_per_game"]
        if brand in rebounds_by_shoe:
            rebounds_by_shoe[brand].append(rebounds)
        else:
            rebounds_by_shoe[brand] = [rebounds]
    for shoe in rebounds_by_shoe:
        avg_rebounds = ("{:.2f}".format(round(sum(rebounds_by_shoe[shoe])/(len(rebounds_by_shoe[shoe])),2)))
        print(f"{shoe}:  {avg_rebounds}")

# average_rebounds_by_shoe_brand()

# code from Nancy Noyes' review Friday 20240322
# 2 line solution:1st two lines after def or following 4 lines as the most simplistic yet verbose
# def get_teams():
#     teams = game_dict().values()
#     return [team for team in teams]
    # team_list = [] 
    # for team in teams:
    #     team_list.append(team["team_name"])
    # return team

# 1st line after def: list comp/1 liner solution or following 3 lines more verbose solution
# def get_all_players():
# return [player for team in get_teams() for player in team["players"]]
    # all_players = []
    # for team in get_teams():
    #     for player in team["players"]:
    #         all_players.append(player)

# Lab methods
# def num_points_per_game(name):
    # for player in get_all_players():
    #     if player["name"] == name:
    #         return player["points_per_game"]
    
    # return next(player["points_per_game"] for player in get_all_players() if player["name"] == name)
