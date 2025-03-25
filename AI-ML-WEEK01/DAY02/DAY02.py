import numpy as np;

#ndom Float Numbers
#Generate random floats between 0 and 1
random_floats = np.random.rand(3,3)
print("Random floates (0 to 1):\n",random_floats)


#Random Integers
#Generate random integers between low and high
random_integers = np.random.randint(1,100,size=(3,3))

print("Random integers (1 to 99):\n",random_integers)

#Standard Normal Distribution
#Data that follows a bell curve (mean=0, std=1)
random_normals = np.random.randn(3,3);
print("Random numners from standard normal distribution:\n",random_normals)

#Seeding for Reproducibility
#Seed makes sure you get the same random numbers every #time (useful in AI experiments)

np.random.seed(42)
reprodusible_random = np.random.rand(3,3)

print("Reproducible random numbers:\n",reprodusible_random)

#Shuffle & Permutations
#Shuffle data (great for training datasets)
array = np.arange(10)
np.random.shuffle(array)
print("Shuffled array:\n",array)

#Random permutation (doesnt change original)
prem_array = np.random.permutation(10)
print("Random permutation:\n",prem_array)

#Fake Dataset Generator (Challenge!)
#🔥 Try generating 100 random samples:

#Each sample has 2 features → like (height, weight)
#Values between 0 and 100

data = np.random.randint(0,100,size=(100,2))
print("Fake AI dateset(100 samples, 2 features):\n",data)


#Summary:
#You can now:

#Generate synthetic data
#Control randomness (seed)
#Simulate real datasets for ML
#Shuffle data for training/testing