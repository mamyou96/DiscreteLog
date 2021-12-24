# DiscreteLog
In this project, I find an algorithm to compute discrete logarithm in Z<sup>*</sup><sub>p</sub>, when p is a prime number such that p = 2<sup>n</sup> + 1 for some n. More precisely, for a given prime number p, generator g and arbitrary y in Zp∗, we want to calculate x such that g<sup>x</sup> = y mod p. 
Let x = b<sub>n−1</sub>2<sup>n−1</sup> + b<sub>n−2</sub>2<sup>n−2</sup> + ... + b<sub>1</sub>2 + b<sub>0</sub> be the binary representation of x.
## Part 1
Calculate the least significant bit of x, i.e. b<sub>0</sub>, for each of the queries. ==> For each query, output the LSB of x, i.e. b<sub>0</sub>, in a separate line such that g<sup>x</sup> = y mod p.
## Part 2
Calculate the 2 least significant bits of x, i.e. b<sub>1</sub>b<sub>0</sub>, for each of the queries. ==> For each query, output the 2 LSB’s of x, i.e. b<sub>1</sub>b<sub>0</sub>, in a separate line such that g<sup>x</sup> = y mod p.
## Part 3
Calculate x for each of the queries. ==> For each query, output x in a seperate line such that g<sup>x</sup> = y mod p.
