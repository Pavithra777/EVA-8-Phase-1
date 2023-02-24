**Custom ResNet architecture for CIFAR10**

![image](https://user-images.githubusercontent.com/52197131/219818005-1473231b-0651-4f33-bf78-59a13e0b985f.png)


**RECEPTIVE FIELD CALCULATION**


![image](https://user-images.githubusercontent.com/52197131/219817397-d423cf01-8505-4f29-b56f-a22994d312b3.png)

Here RF is more than the size of the image.

A large RF can hold different size and variants as a template


**ORIGINAL IMAGE**

![image](https://user-images.githubusercontent.com/52197131/219788572-1ff666dd-f3f5-4dca-b3f2-c35bf9c6f0ca.png)


**AUGMENTED IMAGE**

![image](https://user-images.githubusercontent.com/52197131/219641403-47e9f844-78e0-4b36-acc4-bdeb9b0c4501.png)




**LR FINDER**


Number of images = 60000
Batch size = 512

**num_iterations = ceil(60000 / 512) = 118**

![image](https://user-images.githubusercontent.com/52197131/219814572-c57b3dc1-e934-44fe-8b39-efa82828cba7.png)


![image](https://user-images.githubusercontent.com/52197131/219640252-9b7beb33-fa6c-4463-8f6f-0d09b7a6c3a3.png)




**ONE CYCLE POLICY SCHEDULER**
  
  1. Total epoch is 24
  2. The learning rate is increased linearly from LRMIN to LRMAX during the first 5 epochs.
  3. The learning rate is decreased linearly from LRMAX to LRMIN during the remaining 19 epochs.
  4. pct_start to the fraction of steps for the increasing phase (5/24 in this case)

![image](https://user-images.githubusercontent.com/52197131/221265541-3a28991d-1602-4900-b4b3-c108a74bc593.png)




**TRAINING LOG**

EPOCH: 1
Batch_id=97 Loss=1.70769 Accuracy=38.41: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 1.3596, Accuracy: 5059/10000 (50.59%)

EPOCH: 2
Batch_id=97 Loss=1.27974 Accuracy=54.13: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]

 Test set : Average loss: 1.1787, Accuracy: 5832/10000 (58.32%)

EPOCH: 3
Batch_id=97 Loss=1.11969 Accuracy=60.21: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]

 Test set : Average loss: 1.0611, Accuracy: 6258/10000 (62.58%)

EPOCH: 4
Batch_id=97 Loss=1.00911 Accuracy=64.37: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.9487, Accuracy: 6635/10000 (66.35%)

EPOCH: 5
Batch_id=97 Loss=0.92347 Accuracy=67.59: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.9181, Accuracy: 6789/10000 (67.89%)

EPOCH: 6
Batch_id=97 Loss=0.85339 Accuracy=70.03: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.8364, Accuracy: 7056/10000 (70.56%)

EPOCH: 7
Batch_id=97 Loss=0.80574 Accuracy=71.54: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]

 Test set : Average loss: 0.7891, Accuracy: 7254/10000 (72.54%)

EPOCH: 8
Batch_id=97 Loss=0.76008 Accuracy=73.52: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.7367, Accuracy: 7426/10000 (74.26%)

EPOCH: 9
Batch_id=97 Loss=0.71154 Accuracy=75.23: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.7690, Accuracy: 7351/10000 (73.51%)

EPOCH: 10
Batch_id=97 Loss=0.67341 Accuracy=76.53: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6894, Accuracy: 7617/10000 (76.17%)

EPOCH: 11
Batch_id=97 Loss=0.64597 Accuracy=77.33: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]

 Test set : Average loss: 0.6843, Accuracy: 7650/10000 (76.50%)

EPOCH: 12
Batch_id=97 Loss=0.61245 Accuracy=78.79: 100%|██████████| 98/98 [00:25<00:00,  3.86it/s]

 Test set : Average loss: 0.6483, Accuracy: 7791/10000 (77.91%)

EPOCH: 13
Batch_id=97 Loss=0.58854 Accuracy=79.66: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6239, Accuracy: 7863/10000 (78.63%)

EPOCH: 14
Batch_id=97 Loss=0.56631 Accuracy=80.30: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.6285, Accuracy: 7802/10000 (78.02%)

EPOCH: 15
Batch_id=97 Loss=0.54459 Accuracy=80.97: 100%|██████████| 98/98 [00:25<00:00,  3.88it/s]

 Test set : Average loss: 0.6298, Accuracy: 7889/10000 (78.89%)

EPOCH: 16
Batch_id=97 Loss=0.52151 Accuracy=81.87: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6073, Accuracy: 7946/10000 (79.46%)

EPOCH: 17
Batch_id=97 Loss=0.50432 Accuracy=82.58: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.5729, Accuracy: 8105/10000 (81.05%)

EPOCH: 18
Batch_id=97 Loss=0.48069 Accuracy=83.30: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.5533, Accuracy: 8096/10000 (80.96%)

EPOCH: 19
Batch_id=97 Loss=0.46570 Accuracy=83.81: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5515, Accuracy: 8151/10000 (81.51%)

EPOCH: 20
Batch_id=97 Loss=0.45026 Accuracy=84.55: 100%|██████████| 98/98 [00:25<00:00,  3.86it/s]

 Test set : Average loss: 0.5519, Accuracy: 8159/10000 (81.59%)

EPOCH: 21
Batch_id=97 Loss=0.43350 Accuracy=85.04: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5602, Accuracy: 8103/10000 (81.03%)

EPOCH: 22
Batch_id=97 Loss=0.42451 Accuracy=85.21: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.5493, Accuracy: 8134/10000 (81.34%)

EPOCH: 23
Batch_id=97 Loss=0.40864 Accuracy=85.94: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.5270, Accuracy: 8238/10000 (82.38%)

EPOCH: 24
Batch_id=97 Loss=0.38941 Accuracy=86.54: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5196, Accuracy: 8280/10000 (82.80%)
 
 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



