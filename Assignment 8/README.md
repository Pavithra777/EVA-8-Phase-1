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


**Selected LR = ler_rate = 0.0035237780584504125** 




**ONE CYCLE POLICY SCHEDULER**
  
  1. Total epoch is 24
  2. The learning rate is increased linearly from LRMIN to LRMAX during the first 5 epochs.
  3. The learning rate is decreased linearly from LRMAX to LRMIN during the remaining 19 epochs.
  4. pct_start to the fraction of steps for the increasing phase (5/24 in this case)

![image](https://user-images.githubusercontent.com/52197131/219814459-d2067978-ad2b-4986-9ab1-e8018d1f47c8.png)



**TRAINING LOG**


EPOCH: 1
Batch_id=97 Loss=1.70637 Accuracy=38.62: 100%|██████████| 98/98 [00:25<00:00,  3.90it/s]

 Test set : Average loss: 1.3549, Accuracy: 5086/10000 (50.86%)

EPOCH: 2
Batch_id=97 Loss=1.27590 Accuracy=54.43: 100%|██████████| 98/98 [00:25<00:00,  3.88it/s]

 Test set : Average loss: 1.1363, Accuracy: 5966/10000 (59.66%)

EPOCH: 3
Batch_id=97 Loss=1.11851 Accuracy=59.98: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 1.0578, Accuracy: 6281/10000 (62.81%)

EPOCH: 4
Batch_id=97 Loss=1.00525 Accuracy=64.24: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.9322, Accuracy: 6750/10000 (67.50%)

EPOCH: 5
Batch_id=97 Loss=0.92473 Accuracy=67.39: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.8745, Accuracy: 6935/10000 (69.35%)

EPOCH: 6
Batch_id=97 Loss=0.85276 Accuracy=70.17: 100%|██████████| 98/98 [00:26<00:00,  3.75it/s]

 Test set : Average loss: 0.8299, Accuracy: 7101/10000 (71.01%)

EPOCH: 7
Batch_id=97 Loss=0.80236 Accuracy=71.80: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.8201, Accuracy: 7124/10000 (71.24%)

EPOCH: 8
Batch_id=97 Loss=0.74825 Accuracy=73.88: 100%|██████████| 98/98 [00:25<00:00,  3.80it/s]

 Test set : Average loss: 0.7421, Accuracy: 7468/10000 (74.68%)

EPOCH: 9
Batch_id=97 Loss=0.70059 Accuracy=75.72: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.7082, Accuracy: 7571/10000 (75.71%)

EPOCH: 10
Batch_id=97 Loss=0.67117 Accuracy=76.49: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.7082, Accuracy: 7584/10000 (75.84%)

EPOCH: 11
Batch_id=97 Loss=0.64008 Accuracy=77.69: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6612, Accuracy: 7702/10000 (77.02%)

EPOCH: 12
Batch_id=97 Loss=0.61193 Accuracy=78.58: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.6328, Accuracy: 7799/10000 (77.99%)

EPOCH: 13
Batch_id=97 Loss=0.58709 Accuracy=79.54: 100%|██████████| 98/98 [00:25<00:00,  3.80it/s]

 Test set : Average loss: 0.6265, Accuracy: 7832/10000 (78.32%)

EPOCH: 14
Batch_id=97 Loss=0.55932 Accuracy=80.63: 100%|██████████| 98/98 [00:26<00:00,  3.76it/s]

 Test set : Average loss: 0.6246, Accuracy: 7875/10000 (78.75%)

EPOCH: 15
Batch_id=97 Loss=0.53518 Accuracy=81.49: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6102, Accuracy: 7910/10000 (79.10%)

EPOCH: 16
Batch_id=97 Loss=0.51333 Accuracy=82.15: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5767, Accuracy: 8008/10000 (80.08%)

EPOCH: 17
Batch_id=97 Loss=0.49996 Accuracy=82.68: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]

 Test set : Average loss: 0.5804, Accuracy: 8041/10000 (80.41%)

EPOCH: 18
Batch_id=97 Loss=0.47911 Accuracy=83.40: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5528, Accuracy: 8084/10000 (80.84%)

EPOCH: 19
Batch_id=97 Loss=0.46414 Accuracy=83.81: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5439, Accuracy: 8158/10000 (81.58%)

EPOCH: 20
Batch_id=97 Loss=0.44791 Accuracy=84.43: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5386, Accuracy: 8198/10000 (81.98%)

EPOCH: 21
Batch_id=97 Loss=0.43078 Accuracy=85.16: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5817, Accuracy: 8034/10000 (80.34%)

EPOCH: 22
Batch_id=97 Loss=0.42063 Accuracy=85.38: 100%|██████████| 98/98 [00:26<00:00,  3.73it/s]

 Test set : Average loss: 0.5148, Accuracy: 8253/10000 (82.53%)

EPOCH: 23
Batch_id=97 Loss=0.40405 Accuracy=85.90: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5139, Accuracy: 8272/10000 (82.72%)

EPOCH: 24
Batch_id=97 Loss=0.39468 Accuracy=86.39: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5315, Accuracy: 8231/10000 (82.31%)

 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



