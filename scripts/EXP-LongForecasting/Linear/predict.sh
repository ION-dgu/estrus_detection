if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
seq_len=168
model_name=NLinear

######################
# 변경할 수 있는 조건들
# --is_training : 새로이 모델을 학습시키고 싶으신 경우 1로 수정해주시면 됩니다. 학습이 아닌 용도에선 0으로 두시면 됩니다.
# --roth_path : 데이터 저장 경로를 바꿀 시 수정해주시면 됩니다.
# --data_path : 사용하고자하는 데이터 파일 이름을 기입해주시면 됩니다.
# --model_id : model id로 새로이 학습을 하실 것이 아니라면 수정하지 않으셔도 됩니다.
#              데이터가 추가되어 모델을 다시 학습하고자 하시면 exp_main.py 파일을 확인하시면 model_id를 알 수 있습니다.
# --seq_len : L 길이로 예측에 사용할 데이터의 길이입니다. 위에 seq_len 값을 수정하시면 됩니다.
# --pred_len : T 길이로 예측하고자 할 길이입니다. 단위는 10분으로 원하시는 값으로 수정해주시면 됩니다.
# 나머지 값들은 수정하시면 안됩니다.

python -u run_longExp.py \
  --is_training 0 \
  --root_path ./dataset/ \
  --data_path cow_new.csv \
  --model_id cow_$seq_len \
  --model $model_name \
  --data custom \
  --features MS \
  --seq_len $seq_len \
  --pred_len 6 \
  --des 'Exp' \
  --itr 1 --batch_size 1024 --learning_rate 0.0005 >logs/LongForecasting/$model_name'_'cow_$seq_len'_'avg.log
