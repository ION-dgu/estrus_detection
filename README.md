This is a github repository that modifies the code in “Are Transformers Effective for Time Series Forecasting?” and applies it to other datasets.

The source of the existing code can be found at the link below.

# Are Transformers Effective for Time Series Forecasting? (AAAI 2023)

This repo is the official Pytorch implementation of LTSF-Linear: "[Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/pdf/2205.13504.pdf)". 

## Requirements

numpy==1.19.5

torch==1.9.0+cu111

torchaudio==0.9.0

torchvision==0.10.0+cu111

pandas==1.1.5

sklearn==0.24.2

# The changed source files and contents are below.

run_longExp.py

It was used to modify the default value of the passed argument.

exp_main.py

Modified and added output result files and metrics.

data_loader.py

There was data preprocessing and border adjustment.

train.sh

This is a newly created sh file for execution.


## Citing

If you find this repository useful for your work, please consider citing it as follows:

```bibtex
@inproceedings{Zeng2022AreTE,
  title={Are Transformers Effective for Time Series Forecasting?},
  author={Ailing Zeng and Muxi Chen and Lei Zhang and Qiang Xu},
  journal={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2023}
}
```

Please remember to cite all the datasets and compared methods if you use them in your experiments.

## Update

# train, predict 실행 파일 분리

scripts/EXP-LongForecasting/Linear 폴더 안에 train.sh, predict.sh 파일이 있습니다.

첫 모델을 학습시킬 땐 train.sh 파일을 실행시켜주시면 됩니다.

이미 학습된 모델이 있으시다면 predict.sh 파일을 실행시켜주시면 됩니다.

실행은 전체 폴더에서 sh scripts/EXP-LongForecasting/Linear/실행파일.sh 를 입력하시면 가능합니다.

# 소요시간

위내온도, X,Y,Z,Total 가속도값 13개를 전부 활용해 모델을 학습할 시 소요되는 시간은 아래와 같았습니다.
![모든이미지_소요시간](https://github.com/ION-dgu/estrus_detection/blob/master/train_time.png)

# 2 종류의 data

위내온도, 활동량 2가지 데이터를 사용해 모델을 사용한다고 하여 사용한 데이터가 2개일때의 성능과 소요시간을 측정해봤습니다.

![소요시간](https://github.com/ION-dgu/estrus_detection/blob/master/train_time_2columns.png)
![성능](https://github.com/ION-dgu/estrus_detection/blob/master/result_2columns.png)

# 예측 이미지

테스트 시 예측 결과에 대한 이미지가 별도의 실행 없이 preds.png 파일로 생성됩니다.

![테스트결과이미지](https://github.com/ION-dgu/estrus_detection/blob/master/preds.png)

