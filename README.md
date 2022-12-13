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

## User 이미지로 성능 확인하기
이 모델에는 User가 가진 이미지로 classification을 확인하는 코드가 포함되어 있지 않다... 그래서 내가 만들었다...<br />
```
Data_making.py
python Test_LHC_video.py
```

Data_making 에서는 비디오를 입력 받아서 정중앙을 기준으로 (225,225) 사이즈로 이미지를 캡쳐한 뒤 이를 지정된 폴더에 저장한다.
비디오 명, 폴더 명, 파일 경로는 모두 알아서 바꿔주어야 한다.

Test_LHC_video 에서는 User의 이미지를 입력받아서 LHC 모델을 통해 emotion을 classify 한다.
나는 여러장의 이미지를 하나의 폴더에 놓고 전체에 대해 모델을 돌려보는 식으로 구현했다.
여러장의 이미지 각각에 대한 결과값으로 확률과 emotion을 반환하며, 이를 모아 csv 파일로 저장하는 코드까지 들어가있다. 

