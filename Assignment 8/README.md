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
Batch_id=97 Loss=1.70104 Accuracy=38.83: 100%|██████████| 98/98 [00:24<00:00,  3.97it/s]

 Test set : Average loss: 1.3259, Accuracy: 5281/10000 (52.81%)

EPOCH: 2
Batch_id=97 Loss=1.27505 Accuracy=54.40: 100%|██████████| 98/98 [00:25<00:00,  3.92it/s]

 Test set : Average loss: 1.1724, Accuracy: 5799/10000 (57.99%)

EPOCH: 3
Batch_id=97 Loss=1.11105 Accuracy=60.77: 100%|██████████| 98/98 [00:25<00:00,  3.86it/s]

 Test set : Average loss: 1.0332, Accuracy: 6335/10000 (63.35%)

EPOCH: 4
Batch_id=97 Loss=1.00603 Accuracy=64.46: 100%|██████████| 98/98 [00:25<00:00,  3.85it/s]

 Test set : Average loss: 0.9403, Accuracy: 6648/10000 (66.48%)

EPOCH: 5
Batch_id=97 Loss=0.91904 Accuracy=67.68: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.8576, Accuracy: 6985/10000 (69.85%)

EPOCH: 6
Batch_id=97 Loss=0.84901 Accuracy=70.30: 100%|██████████| 98/98 [00:25<00:00,  3.80it/s]

 Test set : Average loss: 0.8221, Accuracy: 7102/10000 (71.02%)

EPOCH: 7
Batch_id=97 Loss=0.79523 Accuracy=71.93: 100%|██████████| 98/98 [00:26<00:00,  3.75it/s]

 Test set : Average loss: 0.7866, Accuracy: 7264/10000 (72.64%)

EPOCH: 8
Batch_id=97 Loss=0.74753 Accuracy=73.90: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.7525, Accuracy: 7365/10000 (73.65%)

EPOCH: 9
Batch_id=97 Loss=0.70784 Accuracy=75.27: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.7299, Accuracy: 7482/10000 (74.82%)

EPOCH: 10
Batch_id=97 Loss=0.67400 Accuracy=76.50: 100%|██████████| 98/98 [00:25<00:00,  3.80it/s]

 Test set : Average loss: 0.7135, Accuracy: 7506/10000 (75.06%)

EPOCH: 11
Batch_id=97 Loss=0.63521 Accuracy=77.98: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.6458, Accuracy: 7756/10000 (77.56%)

EPOCH: 12
Batch_id=97 Loss=0.60621 Accuracy=79.07: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.6441, Accuracy: 7768/10000 (77.68%)

EPOCH: 13
Batch_id=97 Loss=0.58311 Accuracy=79.69: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.6385, Accuracy: 7817/10000 (78.17%)

EPOCH: 14
Batch_id=97 Loss=0.55848 Accuracy=80.56: 100%|██████████| 98/98 [00:25<00:00,  3.78it/s]

 Test set : Average loss: 0.6383, Accuracy: 7819/10000 (78.19%)

EPOCH: 15
Batch_id=97 Loss=0.54127 Accuracy=81.19: 100%|██████████| 98/98 [00:26<00:00,  3.73it/s]

 Test set : Average loss: 0.6071, Accuracy: 7900/10000 (79.00%)

EPOCH: 16
Batch_id=97 Loss=0.51635 Accuracy=82.08: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5797, Accuracy: 8050/10000 (80.50%)

EPOCH: 17
Batch_id=97 Loss=0.49806 Accuracy=82.76: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5628, Accuracy: 8078/10000 (80.78%)

EPOCH: 18
Batch_id=97 Loss=0.48297 Accuracy=83.40: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5866, Accuracy: 8034/10000 (80.34%)

EPOCH: 19
Batch_id=97 Loss=0.46532 Accuracy=84.00: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5547, Accuracy: 8131/10000 (81.31%)

EPOCH: 20
Batch_id=97 Loss=0.44592 Accuracy=84.59: 100%|██████████| 98/98 [00:25<00:00,  3.79it/s]

 Test set : Average loss: 0.5694, Accuracy: 8041/10000 (80.41%)

EPOCH: 21
Batch_id=97 Loss=0.42468 Accuracy=85.57: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5533, Accuracy: 8155/10000 (81.55%)

EPOCH: 22
Batch_id=97 Loss=0.41818 Accuracy=85.64: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5303, Accuracy: 8202/10000 (82.02%)

EPOCH: 23
Batch_id=97 Loss=0.40330 Accuracy=86.14: 100%|██████████| 98/98 [00:26<00:00,  3.75it/s]

 Test set : Average loss: 0.5140, Accuracy: 8251/10000 (82.51%)

EPOCH: 24
Batch_id=97 Loss=0.39187 Accuracy=86.47: 100%|██████████| 98/98 [00:26<00:00,  3.77it/s]

 Test set : Average loss: 0.5047, Accuracy: 8295/10000 (82.95%)

 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



