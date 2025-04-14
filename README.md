# DB-Design

## Purpose of this repo
1. A sandbox for exploring and iterating database schema ideas related to event detection.
2. A space to experiment with code implementations and test early-stage concepts.


## Possession and pass tracking

> This project tries to simulate and analyze positional tracking data for a 5v5 football game using CSV inputs for 3 players and the ball. It includes logic to determine ball possession and detect pass events based on coordinate data.

## Folder Information

📂 Position_data

- Stores the (x, y) coordinates of Player A, Player B, Player C, and the ball.
- Assumption: The coordinates of each tracked entity are provided as separate dataframes, one per frame or time unit.

📂 Components

- It may contain some modular components that are being used in the main script. These can be used for debugging and better understanding the code.

📂 Outputs

- Contains the pass log and possession timelines based on the movement of the ball and player.
