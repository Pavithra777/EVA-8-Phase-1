**Summary**

Training with resnet18 for 20 epochs on the CIFAR10 dataset. Then have have displayed 10 misclassified images and gradcam visualization for the 10 missclassified images.

**Grad-Cam**

Grad-CAM is a deep learning technique used to understand and visualize the regions in a given image that the neural network is looking at to make a prediction.**It provides a heatmap highlighting the parts of the image that contributed the most to the prediction made by the neural network. It is computed using the gradients of the activations of a chosen convolutional layer with respect to the final prediction made by the network.** Grad-CAM helps to better understand the workings of a neural network and to identify potential biases in its decision-making process.


**MAIN repo**

https://github.com/Pavithra777/EVA-8-Phase-1/tree/main/Assignment%207

**model.py**

https://github.com/Pavithra777/Pavithra/blob/main/models/resnet.py

**utils.py**

https://github.com/Pavithra777/Pavithra/blob/main/utils.py

**main.py**

https://github.com/Pavithra777/Pavithra/blob/main/main.py

**Training Log**


EPOCH: 6
Loss=-41266.46875 Batch_id=781 Accuracy=12.79: 100%|██████████| 782/782 [00:52<00:00, 15.00it/s]

Test set: Average loss: -35328.3031, Accuracy: 1394/10000 (13.94%)

EPOCH: 7
Loss=-55666.60546875 Batch_id=781 Accuracy=11.45: 100%|██████████| 782/782 [00:52<00:00, 15.01it/s]

Test set: Average loss: -51742.8702, Accuracy: 1145/10000 (11.45%)

EPOCH: 8
Loss=-76061.1953125 Batch_id=781 Accuracy=11.06: 100%|██████████| 782/782 [00:51<00:00, 15.04it/s]

Test set: Average loss: -73927.7784, Accuracy: 1068/10000 (10.68%)

EPOCH: 9
Loss=-96235.0390625 Batch_id=781 Accuracy=10.93: 100%|██████████| 782/782 [00:52<00:00, 15.01it/s]

Test set: Average loss: -93950.4881, Accuracy: 1026/10000 (10.26%)

EPOCH: 10
Loss=-115385.8359375 Batch_id=781 Accuracy=10.69: 100%|██████████| 782/782 [00:52<00:00, 15.01it/s]

Test set: Average loss: -106742.7668, Accuracy: 1097/10000 (10.97%)

EPOCH: 11
Loss=-126885.5703125 Batch_id=781 Accuracy=10.72: 100%|██████████| 782/782 [00:51<00:00, 15.05it/s]

Test set: Average loss: -132419.5015, Accuracy: 1074/10000 (10.74%)

EPOCH: 12
Loss=-141634.453125 Batch_id=781 Accuracy=10.65: 100%|██████████| 782/782 [00:52<00:00, 15.00it/s]

Test set: Average loss: -149687.6636, Accuracy: 1050/10000 (10.50%)

EPOCH: 13
Loss=-154103.015625 Batch_id=781 Accuracy=10.46: 100%|██████████| 782/782 [00:51<00:00, 15.05it/s]

Test set: Average loss: -159874.6318, Accuracy: 1036/10000 (10.36%)

EPOCH: 14
Loss=-168698.4375 Batch_id=781 Accuracy=10.42: 100%|██████████| 782/782 [00:51<00:00, 15.06it/s]

Test set: Average loss: -161306.5561, Accuracy: 1071/10000 (10.71%)

EPOCH: 15
Loss=-173606.640625 Batch_id=781 Accuracy=10.45: 100%|██████████| 782/782 [00:51<00:00, 15.05it/s]

Test set: Average loss: -175205.7632, Accuracy: 1049/10000 (10.49%)

EPOCH: 16
Loss=-177472.6875 Batch_id=781 Accuracy=10.46: 100%|██████████| 782/782 [00:51<00:00, 15.05it/s]

Test set: Average loss: -176902.5372, Accuracy: 1043/10000 (10.43%)

EPOCH: 17
Loss=-181067.5625 Batch_id=781 Accuracy=10.50: 100%|██████████| 782/782 [00:51<00:00, 15.05it/s]

Test set: Average loss: -172607.0643, Accuracy: 1064/10000 (10.64%)

EPOCH: 18
Loss=-177533.125 Batch_id=781 Accuracy=10.49: 100%|██████████| 782/782 [00:51<00:00, 15.06it/s]

Test set: Average loss: -180730.3492, Accuracy: 1043/10000 (10.43%)

EPOCH: 19
Loss=-181710.875 Batch_id=781 Accuracy=10.43: 100%|██████████| 782/782 [00:53<00:00, 14.71it/s]

Test set: Average loss: -176807.1405, Accuracy: 1056/10000 (10.56%)

**10 Misclassified Images and  GradCam outputs Gallery**

![image](https://user-images.githubusercontent.com/52197131/218266266-2a044199-f906-43a6-b3dc-c96ddef16f06.png)
![image](https://user-images.githubusercontent.com/52197131/218266306-598aa6b6-cb05-47d9-868d-eb304b0c3afc.png)
![image](https://user-images.githubusercontent.com/52197131/218266329-8ca96020-c664-41d9-a1cd-50d87958fe0d.png)
![image](https://user-images.githubusercontent.com/52197131/218266361-3cf5c958-5db1-4cee-83f9-5d8fa3cc3078.png)




