# Science Fair Experiment
Determining the effect of the number of hidden layers and number of neurons/nodes per hidden layer on the accuracy of a feed-forward neural network used to classify MNIST images.

Not so much trying to determine what hyperparameters perform best, but their effect: ie. 60 neurons was the minimum for a 90+ percent acc, etc.

Same number of neurons for all hidden layers in order to prevent exponential increase in number of models:
5 hidden layer with 100 neurons - results in a network with 5 hidden layers that all have 100 neurons - no variation between layers
