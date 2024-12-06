def team_analysis(current_df, team):
    # Filter dataframe for the selected team
    team_df = current_df[current_df['TEAM'] == team]
    team_df = team_df[team_df['Year'] == '2023-24']

    # Calculate team-wide stats
    team_performance = {
        'Total Players': len(team_df['PLAYER'].unique()),
        'Average Fantasy Points': team_df['Fantasy Points'].mean(),
        'Total Fantasy Points': team_df['Fantasy Points'].sum()
    }

    return team_performance