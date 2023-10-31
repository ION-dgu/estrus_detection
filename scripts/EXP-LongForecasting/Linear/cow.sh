if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
seq_len=168
model_name=NLinear

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ \
  --data_path cow_train.csv \
  --model_id cow_$seq_len'_'threshold_0.8 \
  --model $model_name \
  --data custom \
  --features MS \
  --seq_len $seq_len \
  --label_len 6 \
  --pred_len 6 \
  --enc_in 8 \
  --des 'Exp' \
  --itr 1 --batch_size 1024 --learning_rate 0.0005 >logs/LongForecasting/$model_name'_'cow_$seq_len'_'train_pred_6_threshold8.log
  
  # python -u run_longExp.py \
  # --is_training 0 \
  # --root_path ./dataset/ \
  # --data_path cow.csv \
  # --model_id cow_$seq_len'_'threshold_0.7 \
  # --model $model_name \
  # --data custom \
  # --features MS \
  # --seq_len $seq_len \
  # --label_len 6 \
  # --pred_len 6 \
  # --enc_in 8 \
  # --des 'Exp' \
  # --itr 1 --batch_size 1024 --learning_rate 0.0005 >logs/LongForecasting/$model_name'_'cow_$seq_len'_'pred_6_threshold5_notrain.log

# python -u run_longExp.py \
#   --is_training 1 \
#   --root_path ./dataset/ \
#   --data_path cow.csv \
#   --model_id cow_$seq_len'_'threshold_0.6_2 \
#   --model $model_name \
#   --data custom \
#   --features MS \
#   --seq_len $seq_len \
#   --label_len 6 \
#   --pred_len 6 \
#   --enc_in 8 \
#   --des 'Exp' \
#   --itr 3 --batch_size 2048  --learning_rate 0.0005 >logs/LongForecasting/$model_name'_'cow_$seq_len'_'pred_6_threshold5_2.log 

# python -u run_longExp.py \
#   --is_training 1 \
#   --root_path ./dataset/ \
#   --data_path cow.csv \
#   --model_id cow_$seq_len'_'threshold_0.6_3 \
#   --model $model_name \
#   --data custom \
#   --features MS \
#   --seq_len $seq_len \
#   --label_len 6 \
#   --pred_len 6 \
#   --enc_in 8 \
#   --des 'Exp' \
#   --itr 5 --batch_size 512 --learning_rate 0.0005 >logs/LongForecasting/$model_name'_'cow_$seq_len'_'pred_6_threshold5_3.log 