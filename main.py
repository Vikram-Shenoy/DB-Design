import pandas as pd

# === Load CSV files ===
player_a = pd.read_csv("./position_data/player_a_tracking.csv")
player_b = pd.read_csv("./position_data/player_b_tracking.csv")
player_c = pd.read_csv("./position_data/player_c_tracking.csv")
ball = pd.read_csv("./position_data/ball_tracking.csv")

# === Merge all into a single DataFrame by timestamp ===
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

# === Possession Detection ===
def detect_possession(row):
    # Check if ball coordinates match any player's coordinates exactly.
    if (row['ball_x'], row['ball_y']) == (row['player_a_x'], row['player_a_y']):
        return 'A'
    elif (row['ball_x'], row['ball_y']) == (row['player_b_x'], row['player_b_y']):
        return 'B'
    elif (row['ball_x'], row['ball_y']) == (row['player_c_x'], row['player_c_y']):
        return 'C'
    else:
        return None

# Apply the possession detection function row-by-row
df['in_possession'] = df.apply(detect_possession, axis=1)

# Summarize total possession time (in seconds)
possession_summary = df['in_possession'].value_counts().reset_index()
possession_summary.columns = ['player', 'seconds_in_possession']

# Optionally, save the full possession timeline for analysis
df.to_csv("./Outputs/possession_timeline.csv", index=False)
possession_summary.to_csv("./Outputs/possesion_summary.csv", index=False)
# === Pass Detection Logic ===
# The idea here is to detect when possession switches from one player (say, A) to another (say, B)
# Even if there are gaps (None) in between, we want to detect a pass once the ball reaches a new player's position.

pass_events = []
prev_non_none = None  # This holds the last non-null possession (i.e. the player who had it last)

# Iterate over each row (each timestamp)
for idx, row in df.iterrows():
    current_possession = row['in_possession']
    
    # Only consider moments when a player is in possession.
    if pd.notnull(current_possession):
        if prev_non_none is None:
            # First time we see possession, record it.
            prev_non_none = current_possession
        elif current_possession != prev_non_none:
            # Possession changed from prev_non_none to current_possession
            pass_events.append({
                'timestamp': row['timestamp'],
                'from_player': prev_non_none,
                'to_player': current_possession
            })
            # Update the previous player with the new possession
            prev_non_none = current_possession

# Convert the list of pass events to a DataFrame
pass_log = pd.DataFrame(pass_events)

# Optionally, save the pass events to CSV for later use:
pass_log.to_csv("./Outputs/pass_log.csv", index=False)