# CSCI4800_AI_Final_Project

### This will be a record of our progress for working with the deepracer

#### Main goal now: To make sure the deepracer is driving within the track and is able to complete a lap

Progress 11/21 
- learned about reward functions examples and testing on AWS
  - tested two reward functions samples, following the centerline or making sure the deepracer stays between the borders
  - chose to work with the reward function that follows the centerline as the main framework
- added code to reward function framework that makes sure the deepracer doesn't turn off course
  - worked with two hyperparameters, is left of center and steering angle
  - if the deepracer's steering angle is negative (turning left) and is left of center or vice versa, the deepracer will be penalized
  - if the deepracer's steering angle is negative (turning left) and is right of center or vice versa, the deepracer will be rewarded

**Mental Note: if you want to update the reward function, please make a pull request :)**
