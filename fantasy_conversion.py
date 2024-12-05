import pandas as pd 

#taking in the pic16b_nba_stats file and giving back a new df that has the modified fantasy stats conversion
def fantasy_stats(nba_df):
    columns = ['Season', 'Player','Team','Pos', 'G', '2P', '3P','FT', 'TRB', 'AST', 'STL', 'BLK', 'TOV']
    
    #Calculating the fantasy version of each stat 
    nba_df['Year']=nba_df['Season']
    nba_df['TEAM']=nba_df['Team']
    nba_df['PLAYER']=nba_df['Player']
    nba_df['FTM'] = nba_df['FT'] * 1 * nba_df['G'] 
    nba_df['FGM'] = nba_df['2P'] * 2 * nba_df['G'] 
    nba_df['FG3M'] = nba_df['3P'] * 3 * nba_df['G'] 
    nba_df['REB'] = nba_df['TRB'] * 1.2 * nba_df['G'] 
    nba_df['AST'] = nba_df['AST'] * 1.5  * nba_df['G'] 
    nba_df['STL'] = nba_df['STL'] * 2  * nba_df['G'] 
    nba_df['BLK'] = nba_df['BLK'] * 2  * nba_df['G'] 
    nba_df['TOV'] = nba_df['TOV'] * -1  * nba_df['G'] 
    
    #Calculate total fantasy points
    nba_df['Fantasy Points'] = (nba_df['FTM'] +
        nba_df['FG3M'] +
        nba_df['FGM'] +
        nba_df['REB'] + 
        nba_df['AST'] + 
        nba_df['STL'] + 
        nba_df['BLK'] + 
        nba_df['TOV']) 
    
    
    #Sort the DataFrame by TEAM in descending order
    nba_df = nba_df.sort_values(by='TEAM')
    
    return nba_df[['Year', 'PLAYER','TEAM','Pos','G', 'FGM','FG3M','FTM', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'Fantasy Points']]
