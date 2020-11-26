# CSCI4800_AI_Final_Project

**Mental Note: if you want to update the reward function, please make a pull request :)**
**Include Later: add notes about development of project in local environment before using AWS console to train DeepRacer**

### This will be a record of our progress for working with the DeepRacer

#### Main goal now: To make sure the DeepRacer is driving within the track and is able to complete a lap

##### Progress 11/21 
- learned about reward functions examples and testing on AWS
  - tested two reward functions samples, following the centerline or making sure the DeepRacer stays between the borders
  - chose to work with the reward function that follows the centerline as the main framework
- added code to reward function framework that makes sure the DeepRacer doesn't turn off course
  - worked with two hyperparameters, is left of center and steering angle
  - if the DeepRacer's steering angle is negative (turning left) and is left of center or vice versa, the DeepRacer will be penalized
  - if the DeepRacer's steering angle is negative (turning left) and is right of center or vice versa, the DeepRacer will be rewarded

##### Progress 11/25
- added progress hyperparameter to reward function
  - adding more reward if the car progresses more than or equal to 25%
  - add reward based on the progress made (x1.25 to current reward if the DeepRacer has completed 25% of the track)

##### Sources
DeepRacer Reward Functions
- https://towardsdatascience.com/an-advanced-guide-to-aws-deepracer-2b462c37eea
- https://codelikeamother.uk/planning-a-training
- https://youtu.be/rpMus-mj4fo

David Silver Lecture 6 : Value Function Approximation
https://youtu.be/UoPei5o4fps

David Silver Lecture 7 : Policy Gradient Methods
https://youtu.be/KHZVXao4qXs

Proximal Policy Optimization 
https://blogs.oracle.com/datascience/reinforcement-learning%3a-proximal-policy-optimization-ppo 

AWS Deep Racer developer guides
-reward function parameters
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html
-reward function samples
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-examples.html 
-AWS training algorithm
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.html  
