# V6

'''
Cloned V3 using a modified version of V4-2's code. We wanted to implement higher reward initializations 
(i.e., 10.0, 5.0, 1.0, 1e-3) instead of (1.0, 0.5, 0.1, and 1e-6). We also wanted to try adding and subtracting rewards
instead of using multiplication to increase or decrease rewards by a percentage. We will also have a check at the end
of the reward function to see if the reward is negative, and if it is we will change the reward to a small value such
as 1e-6. We wanted to start these changes from a model that had a successful Reward graph such as V3.
'''

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
        reward = 10.0
    elif distance_from_center <= marker_2:
        reward = 5.0
    elif distance_from_center <= marker_3:
        reward = 1.0
    else:
        reward = 1e-3  # likely crashed/ close to off track
      
    # Check if Deepracer is left of center and turning left, give penalty  
    if is_left_of_center == True and steering_angle > 0:
        reward -= 1.0
    # Check if Deepracer is left of center and turning right, give reward
    elif is_left_of_center == True and steering_angle < 0:
        reward += 1.0
        # Check if Deepracer is right of center and turning right, give penalty
    elif is_left_of_center == False and steering_angle < 0:
        reward -= 1.0
    # Check if Deepracer is right of center and turning left, give reward
    elif is_left_of_center == False and steering_angle > 0:
        reward += 1.0
        
    # Reward the deepracer based on progress made after completing 25% of the track.
    if progress >= 25:
        reward = reward + (progress / 100) # 25% -> reward + 0.25 // 60% -> reward + 0.60
    
    # Check if reward is 0 or below and if so make reward a small decimal value    
    if reward <= 0.0:
        reward = 1e-6
    
    return float(reward)
