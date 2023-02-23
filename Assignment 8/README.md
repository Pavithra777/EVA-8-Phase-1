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

![image](https://user-images.githubusercontent.com/52197131/219814459-d2067978-ad2b-4986-9ab1-e8018d1f47c8.png)



**TRAINING LOG**

EPOCH: 1
Batch_id=97 Loss=1.69889 Accuracy=38.97: 100%|██████████| 98/98 [00:25<00:00,  3.89it/s]

 Test set : Average loss: 1.3660, Accuracy: 5060/10000 (50.60%)

EPOCH: 2
Batch_id=97 Loss=1.28067 Accuracy=53.91: 100%|██████████| 98/98 [00:25<00:00,  3.87it/s]

 Test set : Average loss: 1.1545, Accuracy: 5868/10000 (58.68%)

EPOCH: 3
Batch_id=97 Loss=1.12300 Accuracy=60.13: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]

 Test set : Average loss: 1.0312, Accuracy: 6311/10000 (63.11%)

EPOCH: 4
Batch_id=97 Loss=1.01012 Accuracy=64.29: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.9953, Accuracy: 6489/10000 (64.89%)

EPOCH: 5
Batch_id=97 Loss=0.92657 Accuracy=67.37: 100%|██████████| 98/98 [00:25<00:00,  3.77it/s]

 Test set : Average loss: 0.8777, Accuracy: 6868/10000 (68.68%)

EPOCH: 6
Batch_id=97 Loss=0.85843 Accuracy=70.01: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.8225, Accuracy: 7138/10000 (71.38%)

EPOCH: 7
Batch_id=97 Loss=0.80088 Accuracy=71.83: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]

 Test set : Average loss: 0.7958, Accuracy: 7199/10000 (71.99%)

EPOCH: 8
Batch_id=97 Loss=0.75377 Accuracy=73.68: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.7753, Accuracy: 7322/10000 (73.22%)

EPOCH: 9
Batch_id=97 Loss=0.71563 Accuracy=74.95: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.7999, Accuracy: 7202/10000 (72.02%)

EPOCH: 10
Batch_id=97 Loss=0.67523 Accuracy=76.44: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.7088, Accuracy: 7530/10000 (75.30%)

EPOCH: 11
Batch_id=97 Loss=0.64478 Accuracy=77.44: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.6602, Accuracy: 7726/10000 (77.26%)

EPOCH: 12
Batch_id=97 Loss=0.61707 Accuracy=78.38: 100%|██████████| 98/98 [00:25<00:00,  3.86it/s]

 Test set : Average loss: 0.6783, Accuracy: 7700/10000 (77.00%)

EPOCH: 13
Batch_id=97 Loss=0.59122 Accuracy=79.54: 100%|██████████| 98/98 [00:26<00:00,  3.75it/s]

 Test set : Average loss: 0.6426, Accuracy: 7852/10000 (78.52%)

EPOCH: 14
Batch_id=97 Loss=0.56564 Accuracy=80.31: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6153, Accuracy: 7891/10000 (78.91%)

EPOCH: 15
Batch_id=97 Loss=0.53801 Accuracy=81.15: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6090, Accuracy: 7881/10000 (78.81%)

EPOCH: 16
Batch_id=97 Loss=0.51893 Accuracy=81.83: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]

 Test set : Average loss: 0.6093, Accuracy: 7941/10000 (79.41%)

EPOCH: 17
Batch_id=97 Loss=0.50245 Accuracy=82.54: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.6125, Accuracy: 7949/10000 (79.49%)

EPOCH: 18
Batch_id=97 Loss=0.48797 Accuracy=83.04: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5625, Accuracy: 8094/10000 (80.94%)

EPOCH: 19
Batch_id=97 Loss=0.46595 Accuracy=83.88: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5701, Accuracy: 8082/10000 (80.82%)

EPOCH: 20
Batch_id=97 Loss=0.45304 Accuracy=84.42: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5536, Accuracy: 8115/10000 (81.15%)

EPOCH: 21
Batch_id=97 Loss=0.43600 Accuracy=84.72: 100%|██████████| 98/98 [00:26<00:00,  3.76it/s]

 Test set : Average loss: 0.5191, Accuracy: 8222/10000 (82.22%)

EPOCH: 22
Batch_id=97 Loss=0.42278 Accuracy=85.37: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5190, Accuracy: 8217/10000 (82.17%)

EPOCH: 23
Batch_id=97 Loss=0.40519 Accuracy=85.99: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5253, Accuracy: 8197/10000 (81.97%)

EPOCH: 24
Batch_id=97 Loss=0.39167 Accuracy=86.49: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.5059, Accuracy: 8327/10000 (83.27%)
 
 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



