# CSCI4800_AI_Final_Project

### This will be a record of our progress for working with the DeepRacer

#### Main goal now: To make sure the DeepRacer is driving within the track and can consistently complete a lap

**Mental Note: if you want to update the reward function, please make a pull request :)**  
**Include Later: add notes about development of project in local environment before using AWS console to train DeepRacer**  

#### Note: A new version of the DeepRacer training (ie. V3 to V4) means that a new functionality or portion of code was added to a previous version of the training tested to enhance reward function. Description will note which version was cloned to add the new functionality. 
#### Note: A sub version of the DeepRacer training (ie. V3 to V3-1) means that the current reward function for that version had values that were modified to enhance reward function. The sub version of the DeepRacer training could also mean that more training was added to increase the DeepRacer's knowledge and improve on its performance. 

##### Local environment Problems
- add later :)

**Main track trained and evaluated on: re:Invent 2018**

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
- Note for future records for trainings and evaluations: did not evaluate after all trainings if the reward graph did not look good
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

##### Progress 11/28
- trained DeepRacer for 15 minutes each training, evaluated 4-5 trials
- retrained the DeepRacer by cloning V3 and using reward function from V4-2 (V5)
  - the DeepRacer did not improve, got worse as more training was done
- research: changed from multiplication approach to additive approach (reference: Advanced Guide To AWS DeepRacer)
  - article taked about subrewards, if the DeepRacer made a good choice for making a turn but is not moving at optimal speed, the multiplication approach wouldn't reflect that the DeepRacer made a good choice for turning correctly and not care about improving the subrewards for turning. 
  - V6: cloned V3, copied V4-2's code, and modified code from V4-2. Modified the amount of reward given to the DeepRacer for the section of code that worked with is_left_of_center and steering_angle parameters by adding rewards to current reward rather than adding reward based on a factor of the current reward. Wanted to train new code on the last successful training simulation to see if new updates improved the DeepRacer's driving. 
    - after training: there were some zig zags for the reward, training, and evaluation
    - after evaluation: DeepRacer is able to complete between 50-70% of a lap on average
- V7: added functionality where the DeepRacer should drive faster than 1.0 m/s (speed threshold). if the DeepRacer is driving slower than 1.0 m/s, it will be penalized (-0.5), otherwise reward it if it is driving faster than or equal to 1.0 m/s.
  - after training: DeepRacer is definitely driving faster, gets lots of reward for maintaining the speed threshold
  - after evaluation: did worse when adding speed, but the main problem was not the speed, it was how to make accurate turns
- V1-1: we wanted to retrain the reward function with the framework that the DeepRacer stayed within the borders of the track and see if it did well on the reinvent:2018 track (before it was trained on the oval track).
  - after training: the reward function did not do well overall, negative slope
- V8: deleted functionality with is_left_of_center and steering_angle and added in functionality for all_wheels_on_track to give reward if the DeepRacer is on track (+1), and penalize the DeepRacer severly if it goes off track (-2)
  - after training: overall, the slope of the average training completion and evaluation had a positive slope, averaging about 40% completion
  - after evaluation: 3 trials, lap completion between 30% to 45%.
  - was thinking of changing the code that makes sure the DeepRacer is on the track (is left of center and steering angle); main problem was that the DeepRacer would make a decision that would be detrimental when it turns (the car is on the left side of the center and needs to turn left, but the car will steer right to meet the requirement of staying on track
  - plan: since this is the best reward function overall, we plan to train with this reward function for another 15 minutes
    - will adjust hyperparameters if there are any converging values for the track completion (after 15 minutes)
    - train again with updated reward function and hyperparameters
- V8-1: trained V8 again for another 15 minutes and increased the penalty value to -3 if the DeepRacer drives off track
  - after training: steeper positive slope observed, higher completion rate for the training and evaluation
  - after evaluation: DeepRacer was able to complete 2 laps in a row (almost 3 laps!, last lap was 98% completion)
- Maybe next time?: try reward function using closest_waypoints code on AWS developer guide (to improve speed and accuracy of turns?)

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
- better description on explaining input parameters and tuning the hyperparameters (batch size, num epochs, entropy, etc.)  
https://wiki.deepracing.io/Training_the_AWS_DeepRacer
