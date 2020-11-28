# V5
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    is_left_of_center = params['is_left_of_center']
    progress = params['progress']
    
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-6  # likely crashed/ close to off track
      
    # Check if Deepracer is left of center and turning left, give penalty  
    if is_left_of_center == True and steering_angle > 0:
        reward *= 0.9
    # Check if Deepracer is left of center and turning right, give reward
    elif is_left_of_center == True and steering_angle < 0:
        reward *= 1.1
        # Check if Deepracer is right of center and turning right, give penalty
    elif is_left_of_center == False and steering_angle < 0:
        reward *= 0.9
    # Check if Deepracer is right of center and turning left, give reward
    elif is_left_of_center == False and steering_angle > 0:
        reward *= 1.1
        
    # Reward the deepracer based on progress made after completing 25% of the track.
    if progress >= 25:
        reward = reward * (1 + ((progress / 4) / 1000)) # 25% -> 1.0062 // 60% -> 1.015
    
    
    return float(reward)
