
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = 'Final_Project/modules/per_game_stats.csv'
df = pd.read_csv(path)


def filter_dataset(player):
    """
    Filters a given dataset for a specific player and specific columns
    
    It also renames the TRB (Total Rebound) to RB (Rebound).
    
    Parameters
    ---
    player : str
        the player we want to find in the dataset
        
    Returns
    ---
    pandas.DataFrame
        dataframe with the player we found
    
    Examples
    ---
    lebron_pra = filter_dataset('Lebron James')
    kobe_pra = filter_dataset('Kobe Bryant')

    
    """
    # Filters for certain columns
    filtered_dataset = df[['Player', 'Season', 'RSorPO','PTS', 'TRB', 'AST']]
    
    # Renames TRB to RB
    filtered_dataset = filtered_dataset.rename(columns={'TRB': 'RB'}, inplace=False)
    
    # Searches for the given player 
    filtered_dataset = filtered_dataset[filtered_dataset['Player'] == player]
    return filtered_dataset

# Define function for finding PRA in a season
def find_PRA(player, season):
    """
    Filters dataset given a certain season, playoffs or regular, 
    and returns a player's states
    
    Parameters
    -------
    player : str
        player name
    
    season : str
        either regular season or playoffs season
    
    Returns
    ----
    pandas.DataFrame
        a dataframe w/ the player's stats given filtered season
    """
    data = filter_dataset(player)
    return data[data['RSorPO'] == season]

def plot_stat(player, stat, season, title_font=24, x_font=20, y_font=20, 
              x_label_font=16, y_label_font=16):
    """
    Plots a certain stat for a given player
    
    Parameter
    ---------
    player : str
        player name
    stat : str
        the stat we are plotting, either points, rebounds, or assists
    title_font : int, optional
        plot title size
    x_font : int, optional
        font size for the x-axis ticks
    y_font : int, optional
        font size for y-axis ticks
    x_label_font : int, optional
        font size for x-axis label
    y_label_font : int, optional
        font size for y-axis label
    """
    
    # Set figure size and labels
    plt.figure(figsize=(24,12))
    plt.xlabel('Season', fontsize=x_font)
    plt.ylabel(stat , fontsize=y_font)
    plt.title(player + "'s Average " + stat + " Per Season", fontsize=title_font)
    plt.tick_params(axis='x', labelsize=x_label_font)
    plt.tick_params(axis='y', labelsize=y_label_font)

    sns.lineplot(data=find_PRA(player, season), x='Season', y=stat, hue='Player',
                 linewidth=5) 
    
def filter_by_season(season):
    """
    Filters the dataset given the certain season (regular/playoffs)
    with all the players in a dataset
    
    Parameters
    ----------
    season : str
        season to filter by
    
    Returns
    -------
    pandas.DataFrame
        dataframe w/ season type and sorted by year
    """
    
    filtered_df = df[df['RSorPO'] == season]
    filtered_df = filtered_df[['Player', 'Season', 'RSorPO','PTS', 'TRB', 'AST']]
    filtered_df = filtered_df.rename(columns={'TRB': 'RB'}, inplace=False)
    filtered_df = filtered_df.sort_values(by='Season', ascending=True)
    return filtered_df

def all_player_stat_comparison(stat, season):
    """
    compares a certain stat for all players given a certain season
    
    Parameter
    ---------
    stat : str
        the stat to measure
    season : str
        season being compared (regular or playoffs)
    """
    
    # Set figure size and labels
    plt.figure(figsize=(60,30))
    plt.xlabel('Season', fontsize=60)
    plt.ylabel('Points', fontsize=60)
    plt.title("Player Average " + stat + " In " + season, fontsize=68)
    plt.tick_params(axis='x', labelsize=35)
    plt.tick_params(axis='y', labelsize=35)
    plt.xticks(rotation=45)

    sns.lineplot(data=filter_by_season(season), x='Season', y=stat, 
                 linewidth=5, hue='Player')
    plt.legend(fontsize=60)

