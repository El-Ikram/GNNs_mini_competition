import json
import sys
import os

# Usage:
# python update_leaderboard.py TEAM_NAME SCORE

team_name = sys.argv[1]
score = float(sys.argv[2])

leaderboard_path = "leaderboard/leaderboard.json"

# Create leaderboard folder if it doesn't exist
os.makedirs("leaderboard", exist_ok=True)

# Load existing leaderboard
if os.path.exists(leaderboard_path):
    with open(leaderboard_path, "r") as f:
        leaderboard = json.load(f)
else:
    leaderboard = []

# Update or add entry
updated = False
for entry in leaderboard:
    if entry["team"] == team_name:
        entry["score"] = score
        updated = True
        break

if not updated:
    leaderboard.append({
        "team": team_name,
        "score": score
    })

# Sort by score (descending)
leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

# Save leaderboard
with open(leaderboard_path, "w") as f:
    json.dump(leaderboard, f, indent=2)

print("🏆 Leaderboard updated successfully!")
