# CSCI4800_AI_Final_Project

### This will be a record of our progress for working with the DeepRacer

#### Main goal now: To make sure the DeepRacer is driving within the track and is able to complete a lap

**Mental Note: if you want to update the reward function, please make a pull request :)**  
**Include Later: add notes about development of project in local environment before using AWS console to train DeepRacer**  

**Next day: try reward function using closest_waypoints code on AWS developer guide**

##### Progress 11/21 
- trained DeepRacer for 10 minutes each training, evaluated for 3-4 trials
- learned about reward functions examples and testing on AWS
  - tested two reward functions samples, following the centerline (V2) or making sure the DeepRacer stays between the borders (V) -> (trained once for each reward function)
  - chose to work with the reward function that follows the centerline as the main framework 
- V3: added code to reward function framework that makes sure the DeepRacer doesn't turn off course (trained once, adding to main reward function of following center line)
  - worked with two hyperparameters, is left of center and steering angle
  - if the DeepRacer's steering angle is negative (turning left) and is left of center or vice versa, the DeepRacer will be penalize (decrease reward by 0.8)
  - if the DeepRacer's steering angle is negative (turning left) and is right of center or vice versa, the DeepRacer will be rewarded (increase reward by 1.4)
- in total, for the main reward function chosen, we trained for a total of 20 minutes

##### Progress 11/25
- trained DeepRacer for 15 minutes each training, evaluated for 4 trials
- did not evaluate after all trainings if the reward graph did not look good
- V4: added progress hyperparameter to reward function (trained with this function)
  - adding more reward if the car progresses more than or equal to 25%
  - add reward based on the progress made (x1.25 to current reward if the DeepRacer has completed 25% of the track)  
  - reward = reward x (1 + (progress / 100))  
  - problem: DeepRacer would not progress after doing a turn, it would continually go off track after turning  
  - we think that the problem was that we gave the DeepRacer too much reward if it made some progress, so the more reward it got the worse its results  
- changed reward function using progress hyper parameter to reduce the amount of reward that the DeepRacer earns  
  - V4-1: first we reduced the amount of reward for the progress (reward = reward x (1 + (progress / 4) / 100)) and penalized the DeepRacer even more when it 
    was farthest away from the center line (reward = 1e-6) -> (trained with this update)  
  - V4-2: then we reduced the amount of reward even more (reward = reward x (1 + (progress / 4) / 1000)) and changed the amount of reward/penalty for when the 
    DeepRacer is within the track or moving away from the track (stay within track, increase by 1.1 x reward; go off track, decrease to 0.9 x reward)
    -> (trained with this update)
- so far, trained DeepRacer for 45 minutes making incremental changes to the reward function
- final updated reward function did not go well, the evaluation was worse than when it was evaluated at V4-1

##### Sources
DeepRacer Reward Functions 
- https://towardsdatascience.com/an-advanced-guide-to-aws-deepracer-2b462c37eea
- https://codelikeamother.uk/planning-a-training
- https://youtu.be/rpMus-mj4fo
- adding reward for progress: https://github.com/Usin2705/DeepRacer

David Silver Lecture 6 : Value Function Approximation  
https://youtu.be/UoPei5o4fps

David Silver Lecture 7 : Policy Gradient Methods  
https://youtu.be/KHZVXao4qXs

Proximal Policy Optimization   
https://blogs.oracle.com/datascience/reinforcement-learning%3a-proximal-policy-optimization-ppo 

AWS Deep Racer developer guides  
- reward function parameters  
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html
- reward function samples  
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-examples.html 
- AWS training algorithm  
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.html  
- better description on tuning the hyperparameters (batch size, num epochs, entropy, etc.)  
https://gabemaldonado.dev/ReinforcementLearningAWSDeepRacer/  
