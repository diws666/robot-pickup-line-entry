#!/usr/bin/env python3
"""Write the robot pickup line entry to /output/entry.txt."""

PICKUP = "I ran a million simulations of asking you out. In every single one, you said yes."  # 81 characters

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(PICKUP)
