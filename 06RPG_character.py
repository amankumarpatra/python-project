# =====================================================================
# PROJECT: RPG Character Creator
# PURPOSE: Demonstrates input validation (Guard Clauses), type checking,
#          and dynamic string formatting for a UI-like output.
# =====================================================================

# Visual constants for the character stat bars
FULL_DOT = '●'
EMPTY_DOT = '○'

def create_character(name, strength, intelligence, charisma):
    """
    Validates character stats and returns a formatted stat sheet.
    
    Rules:
    - Name: Non-empty string, max 10 chars, no spaces.
    - Stats: Integers between 1 and 4.
    - Total: Must sum exactly to 7 points.
    """

    # --- 1. NAME VALIDATION ---
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"
    
    if ' ' in name:
        return "The character name should not contain spaces"

    # --- 2. DATA TYPE VALIDATION ---
    # Ensures all stats are integers before performing math
    if (not isinstance(strength, int) or 
        not isinstance(intelligence, int) or 
        not isinstance(charisma, int)):
        return "All stats should be integers"
    
    # --- 3. VALUE RANGE VALIDATION ---
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    # --- 4. GAME BALANCE VALIDATION ---
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    # --- 5. FORMATTED OUTPUT ---
    # Generates a stat bar of 10 dots for each attribute
    # Example: 4 points = ●●●●○○○○○○
    return (
        f"{name}\n"
        f"STR {FULL_DOT * strength + EMPTY_DOT * (10 - strength)}\n"
        f"INT {FULL_DOT * intelligence + EMPTY_DOT * (10 - intelligence)}\n"
        f"CHA {FULL_DOT * charisma + EMPTY_DOT * (10 - charisma)}"
    )

# Test the function
print(create_character('Ren', 4, 2, 1))
