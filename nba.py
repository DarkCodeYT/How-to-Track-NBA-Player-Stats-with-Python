from nba_api.stats.endpoints import PlayerGameLog
from nba_api.stats.static import players
from tabulate import tabulate
import pandas as pd

def search_player(name):
    # Search for the player
    player = players.find_players_by_full_name(name)
    if not player:
        return "Player not found"
    return player[0]

def get_stats(player_id):
    # Get the games from the current season
    gamelog = PlayerGameLog(player_id=player_id, season='2024-25')
    df = gamelog.get_data_frames()[0]
    
    # Select and rename relevant columns
    df_selected = df[['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST', 'MIN']]
    df_selected.columns = ['Date', 'Matchup', 'Points', 'Rebounds', 'Assists', 'Minutes']
    
    return df_selected

def main():
    # Ask for the player's name
    name = input("Enter the player's name (example: LeBron James): ")
    
    # Search for the player
    player = search_player(name)
    if isinstance(player, str):
        print(player)
        return
    
    # Get and display statistics
    try:
        stats = get_stats(player['id'])
        print(f"\nStatistics for {player['full_name']} (Season 2024-25):")
        print(tabulate(stats, headers='keys', tablefmt='grid', showindex=False))
        
    except Exception as e:
        print(f"Error retrieving data: {e}")

if __name__ == "__main__":
    main()