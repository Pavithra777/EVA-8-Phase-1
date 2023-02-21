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
Batch_id=97 Loss=1.70254 Accuracy=38.45: 100%|██████████| 98/98 [00:24<00:00,  3.98it/s]

 Test set : Average loss: 1.3339, Accuracy: 5196/10000 (51.96%)

EPOCH: 2
Batch_id=97 Loss=1.26817 Accuracy=54.79: 100%|██████████| 98/98 [00:24<00:00,  4.01it/s]

 Test set : Average loss: 1.2202, Accuracy: 5648/10000 (56.48%)

EPOCH: 3
Batch_id=97 Loss=1.10898 Accuracy=60.75: 100%|██████████| 98/98 [00:24<00:00,  3.96it/s]

 Test set : Average loss: 1.0354, Accuracy: 6332/10000 (63.32%)

EPOCH: 4
Batch_id=97 Loss=1.00654 Accuracy=64.57: 100%|██████████| 98/98 [00:25<00:00,  3.91it/s]

 Test set : Average loss: 0.9509, Accuracy: 6651/10000 (66.51%)

EPOCH: 5
Batch_id=97 Loss=0.91987 Accuracy=67.52: 100%|██████████| 98/98 [00:25<00:00,  3.86it/s]

 Test set : Average loss: 0.9333, Accuracy: 6729/10000 (67.29%)

EPOCH: 6
Batch_id=97 Loss=0.85476 Accuracy=69.96: 100%|██████████| 98/98 [00:25<00:00,  3.87it/s]

 Test set : Average loss: 0.8240, Accuracy: 7113/10000 (71.13%)

EPOCH: 7
Batch_id=97 Loss=0.79605 Accuracy=72.01: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.7897, Accuracy: 7235/10000 (72.35%)

EPOCH: 8
Batch_id=97 Loss=0.74747 Accuracy=73.83: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.7378, Accuracy: 7429/10000 (74.29%)

EPOCH: 9
Batch_id=97 Loss=0.70423 Accuracy=75.33: 100%|██████████| 98/98 [00:26<00:00,  3.76it/s]

 Test set : Average loss: 0.7149, Accuracy: 7486/10000 (74.86%)

EPOCH: 10
Batch_id=97 Loss=0.67419 Accuracy=76.50: 100%|██████████| 98/98 [00:25<00:00,  3.80it/s]

 Test set : Average loss: 0.7045, Accuracy: 7551/10000 (75.51%)

EPOCH: 11
Batch_id=97 Loss=0.63638 Accuracy=77.85: 100%|██████████| 98/98 [00:26<00:00,  3.74it/s]

 Test set : Average loss: 0.6665, Accuracy: 7727/10000 (77.27%)

EPOCH: 12
Batch_id=97 Loss=0.60765 Accuracy=78.85: 100%|██████████| 98/98 [00:25<00:00,  3.84it/s]

 Test set : Average loss: 0.6417, Accuracy: 7812/10000 (78.12%)

EPOCH: 13
Batch_id=97 Loss=0.57955 Accuracy=79.94: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.6227, Accuracy: 7857/10000 (78.57%)

EPOCH: 14
Batch_id=97 Loss=0.55838 Accuracy=80.50: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.6025, Accuracy: 7948/10000 (79.48%)

EPOCH: 15
Batch_id=97 Loss=0.53715 Accuracy=81.41: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5943, Accuracy: 7981/10000 (79.81%)

EPOCH: 16
Batch_id=97 Loss=0.51513 Accuracy=82.18: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5902, Accuracy: 7973/10000 (79.73%)

EPOCH: 17
Batch_id=97 Loss=0.49520 Accuracy=82.96: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5967, Accuracy: 7944/10000 (79.44%)

EPOCH: 18
Batch_id=97 Loss=0.47923 Accuracy=83.44: 100%|██████████| 98/98 [00:26<00:00,  3.74it/s]

 Test set : Average loss: 0.5673, Accuracy: 8118/10000 (81.18%)

EPOCH: 19
Batch_id=97 Loss=0.46246 Accuracy=83.99: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5414, Accuracy: 8113/10000 (81.13%)

EPOCH: 20
Batch_id=97 Loss=0.44719 Accuracy=84.47: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5241, Accuracy: 8205/10000 (82.05%)

EPOCH: 21
Batch_id=97 Loss=0.43321 Accuracy=84.96: 100%|██████████| 98/98 [00:25<00:00,  3.81it/s]

 Test set : Average loss: 0.5509, Accuracy: 8123/10000 (81.23%)

EPOCH: 22
Batch_id=97 Loss=0.41745 Accuracy=85.69: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5177, Accuracy: 8259/10000 (82.59%)

EPOCH: 23
Batch_id=97 Loss=0.40164 Accuracy=86.09: 100%|██████████| 98/98 [00:25<00:00,  3.82it/s]

 Test set : Average loss: 0.5270, Accuracy: 8227/10000 (82.27%)

EPOCH: 24
Batch_id=97 Loss=0.39562 Accuracy=86.26: 100%|██████████| 98/98 [00:25<00:00,  3.83it/s]

 Test set : Average loss: 0.5212, Accuracy: 8219/10000 (82.19%)


 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



