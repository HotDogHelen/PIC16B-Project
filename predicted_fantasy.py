from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_next_fantasy_point(df):
    predictions = []
    
    # Ensure the input data is sorted by 'Year' for proper chronological order
    df = df.sort_values(by=['PLAYER', 'Year'])
    

    
    for player_name in df['PLAYER'].unique():
        # Filter data for the specific player
        player_data = df[df['PLAYER'] == player_name].copy()
        
        # Ensure there's enough data for training
        if len(player_data) < 2:
            continue  # Skip this player if not enough data
        
        # Create the 'NextYearPoints' column (target)
        player_data['NextYearPoints'] = player_data['Fantasy Points'].shift(-1)
        
        # Drop the last row (no target value available for it)
        player_data = player_data.dropna()
        
        # Ensure there's enough data left after dropping NaNs
        if len(player_data) < 2:
            continue
        
        # Define X (features) and y (target)
        X = player_data['Fantasy Points'].values.reshape(-1, 1)
        y = player_data['NextYearPoints'].values
        
        # Split the data into training and testing sets (80/20 split)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train the model (simple linear regression)
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Predict the next year's fantasy points based on the most recent data point
        last_year_points = player_data['Fantasy Points'].iloc[-1]
        next_year_prediction = model.predict([[last_year_points]])[0]
        
        
        # Append the prediction to the list
        predictions.append({'PLAYER': player_name, 'Pred Fantasy Points': next_year_prediction})
        
    
    # Create a DataFrame from the predictions and sort by predicted points in descending order
    predictions_df = pd.DataFrame(predictions)
    predictions_df['Year'] = '2024-25'
    predictions
    next_year_points = predictions_df.sort_values(by='Pred Fantasy Points', ascending=False).reset_index(drop=True)
    
    return next_year_points
