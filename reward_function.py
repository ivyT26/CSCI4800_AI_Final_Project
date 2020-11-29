# V8-3

def reward_function(params):
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10.0
    elif distance_from_center <= marker_2:
        reward = 5.0
    elif distance_from_center <= marker_3:
        reward = 1.0
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    # Reward the deepracer based on progress made after completing 25% of the track.
    if progress >= 25:
        reward = reward + (progress / 100) # 25% -> reward + 0.25 // 60% -> reward + 0.60
        
    # Reward the deepracer if it's speed is higher than 1.0 m/s, otherwise penalize it
    if speed > 0.65:
        reward += 0.5
    else:
        reward -= 0.5
        
    # Check if all wheels are on track, if they are reward deepracer, if not give penalty
    if all_wheels_on_track:
        reward += 1.0
    else:
        reward -= 3.0
    
    # Check if reward is 0 or below and if so make reward a small decimal value    
    if reward <= 0.0:
        reward = 1e-6
    
    return float(reward)
