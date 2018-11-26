## Neural Networks

### Introduction to neural networks

**What is a Neural Network?**

An Artificial Neural Network (ANN) is an information processing paradigm that is inspired by the way biological nervous systems, such as the brain, process information. The key element of this paradigm is the novel structure of the information processing system. It is composed of a large number of highly interconnected processing elements (neurones) working in unison to solve specific problems. ANNs, like people, learn by example. An ANN is configured for a specific application, such as pattern recognition or data classification, through a learning process. Learning in biological systems involves adjustments to the synaptic connections that exist between the neurones. This is true of ANNs as well.

----

**Why use neural networks?**

Neural networks, with their remarkable ability to derive meaning from complicated or imprecise data, can be used to extract patterns and detect trends that are too complex to be noticed by either humans or other computer techniques. A trained neural network can be thought of as an "expert" in the category of information it has been given to analyse. This expert can then be used to provide projections given new situations of interest and answer "what if" questions. Other advantages include:
	1. Adaptive learning: An ability to learn how to do tasks based on the data given for training or initial experience.
	2. Self-Organisation: An ANN can create its own organisation or representation of the information it receives during learning time.
	3. Real Time Operation: ANN computations may be carried out in parallel, and special hardware devices are being designed and manufactured which take advantage of this capability.
	4. Fault Tolerance via Redundant Information Coding: Partial destruction of a network leads to the corresponding degradation of performance. However, some network capabilities may be retained even with major network damage.

----

**Neural networks versus conventional computers**

Neural networks take a different approach to problem solving than that of conventional computers. Conventional computers use an algorithmic approach i.e. the computer follows a set of instructions in order to solve a problem. Unless the specific steps that the computer needs to follow are known the computer cannot solve the problem. That restricts the problem solving capability of conventional computers to problems that we already understand and know how to solve. But computers would be so much more useful if they could do things that we don't exactly know how to do.

Neural networks process information in a similar way the human brain does. The network is composed of a large number of highly interconnected processing elements(neurones) working in parallel to solve a specific problem. Neural networks learn by example. They cannot be programmed to perform a specific task. The examples must be selected carefully otherwise useful time is wasted or even worse the network might be functioning incorrectly. The disadvantage is that because the network finds out how to solve the problem by itself, its operation can be unpredictable.

On the other hand, conventional computers use a cognitive approach to problem solving; the way the problem is to solved must be known and stated in small unambiguous instructions. These instructions are then converted to a high level language program and then into machine code that the computer can understand. These machines are totally predictable; if anything goes wrong is due to a software or hardware fault.

Neural networks and conventional algorithmic computers are not in competition but complement each other. There are tasks are more suited to an algorithmic approach like arithmetic operations and tasks that are more suited to neural networks. Even more, a large number of tasks, require systems that use a combination of the two approaches (normally a conventional computer is used to supervise the neural network) in order to perform at maximum efficiency.

----

### Lecture Notes

[Intro Video](https://cl.ly/0i0E2X0m032k)

![](https://cl.ly/3R2g0x291M0s/Image%202016-08-01%20at%207.40.45%20PM.png "perceptron")

**Perceptron** is a linear function and it computes based on the following example

![alt text](https://cl.ly/0F3s192A210R/Image%202016-08-01%20at%206.07.01%20PM.png "1")
![alt text](https://cl.ly/161a2K2T0g13/Image%202016-08-01%20at%206.07.58%20PM.png "2")

The example above is a perceptron of an AND gate.


#### Quiz: `OR` Gate as a Perceptron

We want `Y` to be the `OR` function. You have to fill in the values for the weights and the theta.

![Perceptron Quiz](https://cl.ly/0V1l0X2V2K0T/Image%202016-08-01%20at%206.11.42%20PM.png "perceptron quiz")

_Step 1:_ we want to move the threshold line down (see image below) in order to include more points inside of the inclusion area which counts as 1 (i.e. True) and only leave one point in the 0 (i.e. False).

![Step 1](https://cl.ly/2h463q1m0W1k/Image%202016-08-01%20at%206.12.52%20PM.png "Step 1")

Now we need a threshold and weights.

Since there are many answers for this, we can try keeping the weights at `1/2` for `W1` and `W2`. However, we'd have to decrease the threshold to `1/4`. 

![Solution](https://cl.ly/472F1p1Q3n06/Image%202016-08-01%20at%206.19.01%20PM.png "solution")


#### Quiz: `NOT` Gate as a Perceptron

Similar to the examples before, we'd like to calculate the weights and theta such that when we have a value of `0` for `X`, response is `True`. When we get `1`, response is `False`.

![Not Gate](https://cl.ly/0U3u0r1F3y3T/Image%202016-08-01%20at%206.22.39%20PM.png "Not Gate")

We need to flip 0 and 1. Which means either the weight or the threshold needs to be negative.

For example, if we have a 0, we want to response with False (below threshold). 

![solution](https://cl.ly/0T2G1g1F1f3r/Image%202016-08-01%20at%206.26.48%20PM.png "solution")


#### Quiz: `XOR` Gate as a Network of Perceptrons

![](https://cl.ly/2C363d142l22/Image%202016-08-01%20at%206.40.42%20PM.png "question")

![](https://cl.ly/0j2I3t3W362u/Image%202016-08-01%20at%206.40.19%20PM.png "answer")


----

### Perceptron Training

We do perceptron training in the following ways: 

- Perceptron Rule
	- Guaranteed response
	- ONLY linearly separable data
- Gradient Decent
	- Robust
	- Converges to local maxima (i.e. locally optimum)

![](https://cl.ly/2M1f2C192O10/Image%202016-08-01%20at%207.58.13%20PM.png "perceptron training")
 
_Note:_ Looks like the major difference between the two is that we only specify the threshold value for one of them.

![](https://cl.ly/3f3y362y2Q1n/Image%202016-08-01%20at%208.01.35%20PM.png "question")

To deal with that, we use a `Sigmoid`, a differentiable function.

![](https://cl.ly/0Y082P2G150R/Image%202016-08-01%20at%208.07.25%20PM.png "sigmoid")

----

### Restriction Bias

[Video](https://cl.ly/1q111Y1F1i0U/Screen%20Recording%202016-08-01%20at%2008.20%20PM.mov)

What are neural nets appropriate for? What is the restriction bias and inductive bias?

Restriction bias tells you about the **representational power** that you're using and about the **set of hypothesis that you're willing to consider**.

For example: 
- **Perceptron:** restricted to half spaces (linearly separable)
- **Sigmoids:** much more complex, not much restriction
 
hmm?

well, we can represent the following:

- Boolean: with network of threshold units
- Continuous
	- "connected", no jumps (discrete) in data
	- we can have patches at the hidden layer and have the outputs simply be the result
- Arbitrary
	- stick together 2 hidden layers 
 
This means multiple hidden layers to represent anything. This is **Dangerous** because you can easily fit this way.

- To solve, you can set a **bounded number of hidden layers** on the also.
- You can also use **cross validation**

Sometimes even with cross validation, we get weird values for errors after a certain point (as seen below)

![](https://cl.ly/2T3o2K1W242Y/Image%202016-08-01%20at%208.25.50%20PM.png "cross validation")

This is because with Neural Networks, sometimes the values being larger can effect the error rates.

_Side Note:_ Do you normalize the data to deal with that?


----

### Preference Bias 

Algorithm's selection of one representation over another.

Which algo?

- Gradient decent
- Initial Weights
	- small random values
		- avoid local minima
		- variability also to avoid local minima
		- small values to avoid overfitting because of large values
 

**Note:** Occam's Razor, entities should not be multiplied unnecessarily. (i.e. no need for more complexity for similar error)


----

### Summary

[Video](https://cl.ly/3g1X3W1e030E)









