# LHC-Net
## Local Multi-Head Channel Self-Attention

최근 연구를 위한 FER SOTA 논문 중 첫번재로 LHC-Net에 대한 실험을 진행하게 되었다. 이 논문은 원래 FER2013 데이터에 대해 표정을 인식하는 알고리즘인데, 나는 Youtube 오픈소스에서 볼 수 있는 데이터셋을 활용해서 실생활에서의 정확도를 확인중이다. 

이 repository에는 원래 모델의 source에 paper review, local 데이터를 추가해서 돌려본 정보등이 포함된다. 

This repository is intended to provide a quick implementation of the LHC-Net and to replicate the results in this [paper](https://arxiv.org/abs/2111.07224) on FER2013 by downloading our trained models or, in case of hardware compatibility, by training the models from scratch. A fully custom training routine is also available.

![Image of LHC_Net](https://github.com/Bodhis4ttva/LHC_Net/blob/main/Images/LHC_Net.jpg)
![Image of LHC_Module2](https://github.com/Bodhis4ttva/LHC_Net/blob/main/Images/LHC_Module2.jpg)

## How to check the replicability of our results without full training
Bit-exact replicability is strongly hardware dependent. Since the results we presented depend on the choice of a very good performing starting ResNet34v2 model, we strongly recommend to run the replicability script before attempting to execute our training protocol which is computational intensive and time consuming.<br />
Execute the following commands in your terminal:
```
python Download_Data.py
python ETL.py
python check_rep.py
```
Ore equivalently:
```
python main_check_rep.py
```
If you get the output "Replicable Results!" you will 99% get our exact result, otherwise if you get "Not Replicable Results. Change your GPU!" you won't be able to get our results.

Please note that *Download_Data.py* will download the FER2013 dataset in .csv format while *ETL.py* will save all the 28709 images of the training set in .jpeg format in order to allow the use of TensorFlow image data generator and save some memory.

**Recommended setup for full replicability: <br />**
Nvidia Geforce GTX-1080ti (other Pascal-based GPUs might work)<br />
GPU Driver 457.51 <br />
Cuda Driver 11.1.1* <br />
CuDNN v8.0.5 - 11.1 <br />
Python 3.8.5 <br />
requirements.txt <br />
<br />
*After Cuda installation rename *C:\...\NVIDIA GPU Computing Toolkit\CUDA\v11.1\bin\cusolver64_11.dll* in *cusolver64_10.dll*

## How to download our trained models and evaluate their performances on FER2013
Execute the following commands in your terminal:<br />
```
python Download_Data.py
python Download_Models.py
python LHC_Downloaded_Eval.py
python Controller_Downloaded_Eval.py
```
Ore equivalently:
```
python main_downloaded.py
```

