Here we are having 3 networks with 3 different Normalization


1. Network with Group Normalization

2. Network with Layer Normalization

3. Network with L1 + BN


model.py has the Network class which accepts parameter normalization_type that can be (GN,LN,BN) and it is imported in the main.ipynb.


**Normalization**

Different features will be at different scale. One feature amplitude might be large like truck wheel and another feature amplitude like cycle wheel might be small.
To bring all the kernel value within a similar scale , we are doing Normalization. So the distance need to be travelled by the kernel value of all the features are similar.

**How To Normalise ?**

1. Using mean of all kernel value, the data is shifted towards zero by subtracting  kernel's value with the mean value. 
2. With the standard deviation of all kernel value , the data is scaled within a range by dividing the zero centered data  by SD.

**Types of Normalization**

![Normalization](https://user-images.githubusercontent.com/52197131/215227352-4e8d167a-e204-4303-913a-f47cee2e3a6c.png)

**Batch Normalization**

A specfic channel is taken from each batch and then normalise. Say taking all the vertical edge channel from each batch.

In the image for Batch Normalization, the batch size is 3 and every third channel from each batch is taken. There will be 1 µ (mean) and 1 σ (SD).

**Layer Normalization**

All the channel from the batch is taken.

In the image for Layer Normalization, for 1 batch there will be 1 µ and 1 SD.

**Group Normalization**

Each batch is seperated into number of groups.

In the image for Group Normalization for 1 batch and 3 group, we will have 3 µ and 3 σ.


**Test/Validation Loss for all 3 models**

![image](https://user-images.githubusercontent.com/52197131/215230890-eeb2e93f-ee5c-4833-a31d-8e7b63c0ca0a.png)


**Test/Validation Accuracy for all 3 models**

![image](https://user-images.githubusercontent.com/52197131/215231169-e5665f53-d502-42c3-aa1c-501ea08f8973.png)



**10 misclassified images for each of the GN models**
![image](https://user-images.githubusercontent.com/52197131/215231811-128a2c6b-0acc-488a-911b-2a8e17d4950e.png)

**10 misclassified images for each of the LN models**
![image](https://user-images.githubusercontent.com/52197131/215231856-cf803eb9-e44e-4454-8d77-6d08cc622b1c.png)


**10 misclassified images for each of the LN models**
![image](https://user-images.githubusercontent.com/52197131/215231875-d36a950c-e745-4868-8689-44023afee2fb.png)







