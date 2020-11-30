# CSCI4800_AI_Final_Project

### This will be a record of our progress for working with the DeepRacer

#### Main goal now: To make sure the DeepRacer is driving within the track and can consistently complete a lap

**Mental Note: if you want to update the reward function, please make a pull request :)**  

#### Note: A new version of the DeepRacer training (ie. V3 to V4) means that a new functionality or portion of code was added to a previous version of the training tested to enhance reward function. Description will note which version was cloned to add the new functionality. 
#### Note: A sub version of the DeepRacer training (ie. V3 to V3-1) means that the current reward function for that version had values that were modified to enhance reward function. The sub version of the DeepRacer training could also mean that more training was added to increase the DeepRacer's knowledge and improve on its performance. 

##### Local environment Problems / Tasks Prior to Using AWS Console to test DeepRacer (before 11/21)
At the time of our proposal we were thinking we would use a Monte Carlo Reinforcement Learning algorithm, but now after learning more in the class and after going over Function Approximation, we feel that we will need to use this method instead. This will be a good fit for our Reinforcement Learning model due to the fact that the deep racer is in a continuous environment with an extremely large number of states and actions that it performs. This is just an idea just because we are unsure if we need to implement our own learning algorithm for the deep racer or if we can adjust the current algorithm used by AWS.

For designing the reward function, we plan on using a greedy approach to train the deep racer. The reward function will be based on how far or close the deep racer is to the center of the track, using the parameter, distance_from_center. We will also use the parameter, all_wheels_on_track, to adjust the reward function if the deep racer is moving away from the center of the track and is at the critical point of moving off track. At this point in the project and due to time constraints, we have narrowed our scope to focus on training the deep racer to stay on the track. If we are able to progress quickly and can get the deep racer to follow the track, we will consider implementing code to adjust the speed of the deep racer to reduce lap times.

Since the project proposal, we have been working on setting up our local environments to train the deep racer using the github repository by Alex Schultz. We also received our Goliath credentials so we can do our local training there. During the process, we ran into a lot of issues with setting up the local environment. 

We had issues deciding which route to go, either doing a dual boot or using a virtual box. We decided to go with the virtual box because it allowed us to get the Ubuntu operating system functional in a quicker and easier way. The downside is that the virtual box is pretty slow. We are still having some issue with our local environment. One problem we had with setting up the environment was that the training log was not displaying after the training started. While doing some research, we figured out that the problem occurred while running ./init.sh, where some of the libraries were incompatible with the installed urllib3. This led to an improper installation of the docker containers. When the training started using ./start.sh, and the command ‘docker ps’ was executed, it only showed two containers, the minio container and the robo container, and the third container, rl_coach, did not exist. We are having trouble figuring out how to fix the current problem. One option was to adjust the settings in the deep racer setup to accommodate for the most recent versions of docker, docker-compose, and nvidia runtime. The other option was figuring out how to install earlier versions of some of these libraries so all the libraries needed to set up the environment are compatible with the set urllib3.

After the project progress proposal, we have joined a deep racing community on Slack, deepracing.io, in order to ask questions and get assistance on setting up the local environment for the project. We were notified that the local environment we were setting up (by Alex Schultz) was a deprecated github, and was advised to use other github repos that were more updated (like mattcamp-local or deepracer-cloud). After setting up the environment using a more updated version of the local environment, we ran into many new problems where the logs produced lots of errors or the visuals on the DeepRacer did not load up correctly and was difficult to debug. Other problems with setting up the local environment were opening up browsers in localhost using a virtual box. Since both of us spent many weeks on setting up the local environment and with the limited time left in the semester to work on the project, we decided to shift to using the AWS DeepRacer console to start working on our reward function for the DeepRacer. 

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
    - train again with updated reward function and hyperparameters (update: did not adjust hyperparameters, did not want to risk a significant change in the model training with little knowledge and information on finding the ideal hyperparameters while modifying the reward function)
- V8-1: trained V8 again for another 15 minutes and increased the penalty value to -3 if the DeepRacer drives off track
  - after training: steeper positive slope observed, higher completion rate for the training and evaluation
  - after evaluation: DeepRacer was able to complete 2 laps in a row (almost 3 laps!, last lap was 98% completion)
- Maybe next time?: try reward function using closest_waypoints code on AWS developer guide (to improve speed and accuracy of turns?)

##### Progress 11/29
- trained DeepRacer for 15 minutes each, evaluated for 5 trials
- this was the day that we added the training logs, evaluation logs, and recorded some demo videos of the evaluations on the models
- also added a folder to hold the pictures of the tracks that we tested the DeepRacer on for reference
- V8-2: let the DeepRacer train for another 15 minutes to see if the improvement was consistent
  - evaluation was pretty consistent with the last evaluation, where the DeepRacer was able to complete 2 laps in a row (almost 3!)
- V8-3: modified the speed threshold because the condition was never met after looking through the logs
  - changed speed if statement to see if the DeepRacer could maintain a speed >= 0.65 m/s rather than > 1.0 m/s
  - after training, the DeepRacer improved in average lap completion and training
    - overall reward did decrease because it was penalized for driving at a speed less than 0.65 m/s
  - after evaluation, the DeepRacer was able to drive a little bit faster. after completing a lap, the time for completion was 28 seconds, compared to the 30 seconds of completion observed in the last few trainings
- V8-4: trained V8-3 model for another 15 minutes
  - training did fluctuate, reward graph had some negative slopes
  - evaluation: did not complete a lap to 100% out of the 5 trials 
- V8-5: trained V8-4 model for another 15 minutes
  - training improved, very positive slope for the training and evaluation, while the overall slope compared to the previous trainings did decrease but had a positive slope when the DeepRacer made good decisions
  - for the evaluation, the DeepRacer was able to complete all 5 laps 100% complete, wherethe fastest time was 26.5 seconds!
- V8-6: trained V8-5 model on a new track, Shanghai Sudu Training, since the overall training and evalauation for the previous few trainings produced good results
  - we decided to chose this track since it was similar to the previous track we trained the model on and we wanted to observe how it would train for the first 15 minutes
  - after training: the DeepRacer did not do well; the overall track completion was about 25%, but the slope of the training and evaluation was not a significant negative slope
  - we assume that the DeepRacer will do better as we train the DeepRacer more on the new track
  - after evaluation: the DeepRacer was able to complete about 60% of the track for 2 of the trials, 52% for 1 of the trials, and the rest were outliers (less than 30%); our observation is that training the DeepRacer model for a longer time will show signs of improvement in lap completion
  - we also want to see if the reward function can help generalize the DeepRacer's knowledge so it can drive accurately on any track as it experiences a variety of tracks; after that and for future work on this project, we could work on improving the lap times or continue focusing on letting the DeepRacer make more accurate decisions (like speeding up on straights or finding optimal steering angle for different turns)
- V8-7: trained V8-6 model on Shanghai Sudu Training track to see if more training using the same reward function would improve the track completion
  - after training: the overall percentage of the track completed did increase from about 25% to about 55%, which shows that the reward function can be used to generalize how to train the DeepRacer on different tracks and improving the accuracy of its decisions overall
  - after evaluation: DeepRacer did well after 30 minutes of training! Out of the 5 trials, the DeepRacer completed 4 laps with 100% completion and consecutively as well!
  - observation: very interesting to note that the DeepRacer did not practice many right turns in the first track (re:Invent 2018), so it did take some training time to learn how to turn right for the Shanghai track

##### Sources
DeepRacer Reward Functions 
- https://towardsdatascience.com/an-advanced-guide-to-aws-deepracer-2b462c37eea
- https://codelikeamother.uk/planning-a-training
- https://youtu.be/rpMus-mj4fo
- https://github.com/scottpletcher/deepracer
- https://medium.com/axel-springer-tech/how-to-win-aws-deepracer-ce15454f594a 
- https://medium.com/vaibhav-malpanis-blog/getting-started-with-deepracer-2020-edition-a7896dd07c48 

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
