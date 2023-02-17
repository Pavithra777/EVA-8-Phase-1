**Custom ResNet architecture for CIFAR10**

1. PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
2.Layer1 -
	1. X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
	2. R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
	3. Add(X, R1)
3.Layer 2 -
	1. Conv 3x3 [256k]
	2. MaxPooling2D
	3. BN
	4. ReLU
4.Layer 3 -
	1.	X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
	2. R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
	3. Add(X, R2)
5.MaxPooling with Kernel Size 4
6.FC Layer 
7.SoftMax

**RECEPTIVE FIELD**

Here RF is more than the size of the image.

A large RF can hold different size and variants as a template

![image](https://user-images.githubusercontent.com/52197131/219817397-d423cf01-8505-4f29-b56f-a22994d312b3.png)


**ORIGINAL IMAGE**

![image](https://user-images.githubusercontent.com/52197131/219788572-1ff666dd-f3f5-4dca-b3f2-c35bf9c6f0ca.png)


**AUGMENTED IMAGE**

![image](https://user-images.githubusercontent.com/52197131/219641403-47e9f844-78e0-4b36-acc4-bdeb9b0c4501.png)




**LR FINDER**

num_iterations = ceil(60000 / 512) = 118

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
 Batch_id=97 Loss=1.67779 Accuracy=40.25: 100%|██████████| 98/98 [00:33<00:00,  2.94it/s]

 Test set : Average loss: 1.3524, Accuracy: 5137/10000 (51.37%)

EPOCH: 2
Batch_id=97 Loss=1.21245 Accuracy=57.03: 100%|██████████| 98/98 [00:33<00:00,  2.94it/s]

 Test set : Average loss: 1.1550, Accuracy: 5910/10000 (59.10%)

EPOCH: 3
Batch_id=97 Loss=1.03333 Accuracy=63.71: 100%|██████████| 98/98 [00:33<00:00,  2.90it/s]

 Test set : Average loss: 1.1429, Accuracy: 5939/10000 (59.39%)

EPOCH: 4
Batch_id=97 Loss=0.90786 Accuracy=68.22: 100%|██████████| 98/98 [00:34<00:00,  2.87it/s]

 Test set : Average loss: 0.9975, Accuracy: 6461/10000 (64.61%)

EPOCH: 5
Batch_id=97 Loss=0.81405 Accuracy=71.71: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]

 Test set : Average loss: 0.8935, Accuracy: 6860/10000 (68.60%)

EPOCH: 6
Batch_id=97 Loss=0.73849 Accuracy=74.36: 100%|██████████| 98/98 [00:35<00:00,  2.79it/s]

 Test set : Average loss: 0.9200, Accuracy: 6820/10000 (68.20%)

EPOCH: 7
Batch_id=97 Loss=0.67076 Accuracy=76.92: 100%|██████████| 98/98 [00:35<00:00,  2.78it/s]

 Test set : Average loss: 0.8097, Accuracy: 7185/10000 (71.85%)

EPOCH: 8
Batch_id=97 Loss=0.62138 Accuracy=78.71: 100%|██████████| 98/98 [00:35<00:00,  2.78it/s]

 Test set : Average loss: 0.8619, Accuracy: 6984/10000 (69.84%)

EPOCH: 9
Batch_id=97 Loss=0.57496 Accuracy=80.24: 100%|██████████| 98/98 [00:34<00:00,  2.82it/s]

 Test set : Average loss: 0.7903, Accuracy: 7260/10000 (72.60%)

EPOCH: 10
Batch_id=97 Loss=0.53116 Accuracy=81.96: 100%|██████████| 98/98 [00:34<00:00,  2.83it/s]

 Test set : Average loss: 0.7499, Accuracy: 7378/10000 (73.78%)

EPOCH: 11
Batch_id=97 Loss=0.48718 Accuracy=83.81: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]

 Test set : Average loss: 0.7780, Accuracy: 7356/10000 (73.56%)

EPOCH: 12
Batch_id=97 Loss=0.45500 Accuracy=84.79: 100%|██████████| 98/98 [00:34<00:00,  2.83it/s]

 Test set : Average loss: 0.7284, Accuracy: 7527/10000 (75.27%)

EPOCH: 13
Batch_id=97 Loss=0.42024 Accuracy=86.19: 100%|██████████| 98/98 [00:34<00:00,  2.83it/s]

 Test set : Average loss: 0.7468, Accuracy: 7459/10000 (74.59%)

EPOCH: 14
Batch_id=97 Loss=0.39286 Accuracy=87.13: 100%|██████████| 98/98 [00:35<00:00,  2.80it/s]

 Test set : Average loss: 0.7249, Accuracy: 7586/10000 (75.86%)

EPOCH: 15
Batch_id=97 Loss=0.36265 Accuracy=88.29: 100%|██████████| 98/98 [00:35<00:00,  2.77it/s]

 Test set : Average loss: 0.7030, Accuracy: 7645/10000 (76.45%)

EPOCH: 16
Batch_id=97 Loss=0.33679 Accuracy=89.18: 100%|██████████| 98/98 [00:35<00:00,  2.78it/s]

 Test set : Average loss: 0.7207, Accuracy: 7599/10000 (75.99%)

EPOCH: 17
Batch_id=97 Loss=0.31645 Accuracy=89.74: 100%|██████████| 98/98 [00:35<00:00,  2.77it/s]

 Test set : Average loss: 0.7253, Accuracy: 7595/10000 (75.95%)

EPOCH: 18
Batch_id=97 Loss=0.28876 Accuracy=90.85: 100%|██████████| 98/98 [00:35<00:00,  2.78it/s]

 Test set : Average loss: 0.7304, Accuracy: 7581/10000 (75.81%)

EPOCH: 19
Batch_id=97 Loss=0.27255 Accuracy=91.48: 100%|██████████| 98/98 [00:35<00:00,  2.79it/s]

 Test set : Average loss: 0.7046, Accuracy: 7674/10000 (76.74%)

EPOCH: 20
Batch_id=97 Loss=0.24944 Accuracy=92.30: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]

 Test set : Average loss: 0.7129, Accuracy: 7674/10000 (76.74%)

EPOCH: 21
Batch_id=97 Loss=0.23245 Accuracy=92.82: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]

 Test set : Average loss: 0.6712, Accuracy: 7769/10000 (77.69%)

EPOCH: 22
Batch_id=97 Loss=0.21238 Accuracy=93.62: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]

 Test set : Average loss: 0.6825, Accuracy: 7810/10000 (78.10%)

EPOCH: 23
Batch_id=97 Loss=0.19505 Accuracy=94.35: 100%|██████████| 98/98 [00:34<00:00,  2.82it/s]

 Test set : Average loss: 0.7102, Accuracy: 7708/10000 (77.08%)

EPOCH: 24
Batch_id=97 Loss=0.17798 Accuracy=94.88: 100%|██████████| 98/98 [00:34<00:00,  2.81it/s]


 
 **Accuracy and Loss**
 
 ![image](https://user-images.githubusercontent.com/52197131/219813542-83bdc314-1792-4a82-b12f-c1c20aee8f1e.png)



