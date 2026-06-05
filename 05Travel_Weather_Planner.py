# =====================================================================
# PROJECT: Travel Weather Planner
# PURPOSE: Demonstrates nested conditional statements, handling "falsy"
#          values, and multi-layered business logic based on user inputs.
# =====================================================================

# --- 1. CONFIGURATION & INITIALIZATION ---
# Input variables representing the user's situation
distance_mi = 4
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

# --- 2. COMMUTE FEASIBILITY LOGIC ---

# CHECK 1: Validate distance input
# If distance_mi is 0, None, or empty, it evaluates to "falsy".
if not distance_mi:
    print(False)

# CHECK 2: Short-distance commute (<= 1 mile)
elif distance_mi <= 1:
    # Walking distance is only feasible if it isn't raining
    if not is_raining:
        print(True)
    else:
        print(False)

# CHECK 3: Medium-distance commute (1 < distance <= 6 miles)
elif distance_mi <= 6:
    # Biking distance requires having a bike AND clear weather
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# CHECK 4: Long-distance commute (> 6 miles)
else:
    # Long distances require motorized transport (car OR ride-share app)
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
