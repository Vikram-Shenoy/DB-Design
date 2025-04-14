import pandas as pd

# Load CSV files
player_a = pd.read_csv("./Position_data/player_a_tracking.csv")
player_b = pd.read_csv("./Position_data/player_b_tracking.csv")
player_c = pd.read_csv("./Position_data/player_c_tracking.csv")
ball = pd.read_csv("./Position_data/ball_tracking.csv")

# Merge all into a single DataFrame by timestamp
df = pd.DataFrame({
    'timestamp': ball['timestamp'],
    'ball_x': ball['x'],
    'ball_y': ball['y'],
    'player_a_x': player_a['x'],
    'player_a_y': player_a['y'],
    'player_b_x': player_b['x'],
    'player_b_y': player_b['y'],
    'player_c_x': player_c['x'],
    'player_c_y': player_c['y']
})

# Possession detection function
def detect_possession(row):
    if (row['ball_x'], row['ball_y']) == (row['player_a_x'], row['player_a_y']):
        return 'A'
    elif (row['ball_x'], row['ball_y']) == (row['player_b_x'], row['player_b_y']):
        return 'B'
    elif (row['ball_x'], row['ball_y']) == (row['player_c_x'], row['player_c_y']):
        return 'C'
    else:
        return None

# Apply possession logic
df['in_possession'] = df.apply(detect_possession, axis=1)

# Summarize total possession time (in seconds)
possession_summary = df['in_possession'].value_counts().reset_index()
possession_summary.columns = ['player', 'seconds_in_possession']


# (Optional) Save full possession timeline to CSV
df.to_csv("./Components/possession_timeline.csv", index=False)
