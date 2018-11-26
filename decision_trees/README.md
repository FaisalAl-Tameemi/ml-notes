
### Intro

In Supervised Learning, we mostly have `Classification` and `Regression`.

**Classification:**

Taking some input, X, and mapping it to some discrete label, usually, True or False, 1 or 0.

For example, given a picture, is it a picture of a number?

**Regression:**

More about continuous value functions. Given a bunch of data, given a new point, will be mapped to a new value.

For example, given a picture, return a count of numbers in the image.

----

Quiz: from the scenarios stated, which examples classification problems and which ones regression problems?

1. Given the credit history of a person applying for a loan. Decide whether or not to give a loan.

2. Given a picture, and the output is whether the person is the picture is of highschool age, kindergarden age or college age.

3. Given a picture as input, and the output is a guess of the age of that person.

https://cl.ly/2y3t013i422n

----

### Classification Learning:

Some terminology:

- **Instances**: the set of input you have

- **Concept**: a function that maps inputs to outputs, ex: pictures to true or false. In other words, it's a connection between objects in the world and whether or not it's a part of a set. Example, is this object part of the set of cars?

- **Target Concept**: what we're trying to represent. For example, in an algo that determines if there's a car in the image. The concept of a car is the target concept.

- **Hypothesis Class:** all the possibilities of the target concept. For example, all things that carry objects / people for A to B are of interest to us, we include them in the Hypothesis Class.

- **Sample:** training set. all of our data paired with their labels. For example, 1000 pictures, each with a label of whether or not it's a picture of a car.

- **Candidate:** the concept that you think might be the target concept. For example, an object that has wheels.

- **Testing Set:** the data you test with.


*Note:* The training is **ALWAYS** different from the testing set because you need to be able to generalize.

----

### Decision Trees

Let's assume a scenario where you have a date. You see a restaurant and your algo should decide if you and your date should enter the restaurant or not?

https://cl.ly/442I1M3l2j3v

Let's figure out how we can define the problem a little further.

- What do we have that we can use to describe a restaurant? i.e. what are the features that are import to us?
  * Cuisine type of restaurant, `type`, ex: italian, indian, etc...
  * The vibe of the restaurant, `atmosphere`, ex: clean, casual, quite, etc..
  * How much you want to impress your date, `boost`. (lol)
  * How much does the restaurant `cost`? We can represent this in categories, like 'expensive' or 'economic', or an exact number (may avg. cost of entree).
  * The level on hunger.
  * ...etc

https://cl.ly/3t1m1S302934

*Note:* In the real-world, you'll encounter data with feature that have no relevance to the solution of the problem. Always consider whether the feature you're looking at are effective ways of solving the problem.

In decision trees, you're trying to arrive to an answer by asking a series of questions and then make a decision.

For example, you see a restaurant and your decision tree would be as follows:

https://cl.ly/192D2p0i1n1x
https://cl.ly/2u2F0b2z2h36

----

### Decision Trees Example

https://cl.ly/1I2e253Q0T1J

----

### Process for building a decision tree:

In simple terms:

1. Pick the "Best" attribute for a question (splits the data in the best possible way)

2. Asked question

3. Follow answer

4. Repeat until you narrow the space of possibilities to one item (i.e. reached an answer)

----

Quiz: "Best" Attribute

Of the 3 possibilities shown, which split do you think is "Best"?

https://cl.ly/3T183l1I2z0O

----

### Expressiveness of Decision Trees

Let's say we want to represent an "AND" gate as a decision tree.

https://cl.ly/1E2j2Q0S1c2n

With an "OR" gate

https://cl.ly/420K3f2b0304

With an "XOR" function

https://cl.ly/420K3f2b0304

With an "N-OR" gate, i.e. any, applied to 3 items

https://cl.ly/3Q3j001z1e3A

*Note:* with this function, the size of the decision tree is linear cause we need N nodes for N possibilities.

With an "X-OR", it's an exponential problem, the number of nodes increase exponentially as possibilities increase.

----

Quiz: How many rows?

https://cl.ly/3O2u0y0U1h3n

----

### ID3

https://cl.ly/2j3K2A2g2k3m

We define "Best" attribute for the split by maximizing information gain.

[read more](https://en.wikipedia.org/wiki/Information_gain_in_decision_trees)

More Entropy is Less Information Gain. Our goal with even decision tree note split is to maximize information gain and minimize entropy (ideally to 0).

----

### ID3 Bias

- Restriction Bias: the restrictions that are applied to the model. for example, based on the data, we may need to use a certain type of algo over the other.

- **Inductive bias** (preference bias):
  - good splits at the top
  - correct over incorrect
  - shorter trees over longer / bigger trees

----

### More resources:

- [Decision Trees // Wikipedia](https://en.wikipedia.org/wiki/Decision_tree)
- [Influence Diagrams // Wikipedia](https://en.wikipedia.org/wiki/Influence_diagram)
- 
