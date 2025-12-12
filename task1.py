# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone = current_followers//milestone_increment
progress_in_milestone = current_followers-(milestone_increment*current_milestone)
total_gained = current_followers - starting_followers
daily_average = total_gained // days_tracked
days_to_milestone = (milestone_increment - progress_in_milestone) // daily_average
weekly_growth = daily_average * 7

# Calculate growth statistics
# TODO

# Calculate projections
# TODO

# Display results with f-strings
print("Creator: DigitalDreamer")
print(f"Current Milestone: {current_milestone}")
print(f"Progress in Milestone: {progress_in_milestone} followers")
print(f"Total Growth: {total_gained} followers")
print(f"Daily Average: {daily_average} followers")
print(f"Days to Next Milestone: {days_to_milestone} days")
print(f"Weekly Growth Projection: {weekly_growth} followers")
