# Project 1 — Temperature Converter
# Author: Getoar Sopa
# Date:   08/05/2026
#
# Instructions:
#   1. Read the README.md in this folder first.
#   2. Fill in the missing lines below.
#   3. Test with: 0°C → 32°F | 100°C → 212°F | -40°C → -40°F

# ── Your solution goes here ───────────────────────────────────────────────────

# Step 1 — Get input from the user and convert to float
celsius = float(input("Enter temperature in Celsius: "))

# Step 2 — Apply the formula
fahrenheit = (celsius * 9/5) + 32

# Step 3 — Print the result using an f-string
print(f"{celsius}°C = {fahrenheit}°F")


# ── Bonus (optional) ─────────────────────────────────────────────────────────
# Add a direction menu (C→F or F→C)
