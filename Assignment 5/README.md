Here we are having 3 networks with 3 different Normalization


1. Network with Group Normalization

2. Network with Layer Normalization

3. Network with L1 + BN


model.py has the Network class which accepts parameter normalization_type that can be (GN,LN,BN) and it is imported in the main.ipynb.


**Normalization**
Different features will be at different scale. One feature amplitude might be large like truck wheel and another feature amplitude like cycle wheel might be small.
To bring all the kernel value within a similar scale. So the distance need to be travelled by the kernel value of all the feature are similar.

**How To Normalise ?**

1. Using mean of all kernel value, the data is shifted towards zero by subtracting mean value with the kernel's value 
2. With the standard deviation , the data is scaled within a range by dividing the zero centered data  by SD.

**Types of Normalization**

![BN](https://user-images.githubusercontent.com/52197131/215224819-081b5a60-f8dd-4b4b-bea5-c70448f16d7a.png)

Batch Normalization : A specfic channel is taken from each batch and then normalise. Say taking all the vertical edge channel from each batch.

In the image for Batch Normalization, the batch size is 3 and every third channel from each batch is taken. There will be 1 µ (mean) and 1 σ (SD).


