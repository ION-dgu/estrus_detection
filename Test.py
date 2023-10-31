import numpy as np
import sklearn
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

mpl.rcParams['axes.unicode_minus'] = False

def adjusted_average_for_matrix(predictions):
    # The total length of the predicted values is the length of the original data plus (6-1).
    total_length = predictions.shape[0] + 5
    averaged_predictions = np.zeros(total_length)
    counts = np.zeros(total_length)
    for i, window_preds in enumerate(predictions):
        start_idx = i
        end_idx = start_idx + 6
        averaged_predictions[start_idx:end_idx] += window_preds
        counts[start_idx:end_idx] += 1
    # Calculate the average value for overlapping parts.
    averaged_predictions /= counts
    # Returns excluding the first 5 and last 5 predicted values.
    return averaged_predictions[5:-5]



print(sklearn.__version__)

test = np.load('./results/cow_168_cow_only_train_threshold_0.8_no_sub_NLinear_custom_ftMS_sl168_ll6_pl6_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy')

# np.putmask(test, test <= 0.8, 0.0)
# np.putmask(test, test > 0.8, 1.0)

#np.savetxt('pred.txt', test.reshape((3,-1)), fmt="%s")

test1 = np.load('./results/cow_168_cow_only_train_threshold_0.8_no_sub_NLinear_custom_ftMS_sl168_ll6_pl6_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/true.npy')
#np.savetxt('true.txt', test1.reshape((3,-1)), fmt="%s")

test2 = np.load('./train_results/pred.npy', allow_pickle=True)


# # print("reshape\n")
# te = test.reshape(5971, -1)
# st = test1.reshape(5971, -1)

# print(te.shape, te.size)
# print(st.shape, st.size)
# print(te.shape)
# print(te[6800:6900][:])
# print("nono\n")
# print(test.size)
# print(te.size)

adjusted_preds_matrix = adjusted_average_for_matrix(te)
test_true = adjusted_average_for_matrix(st)
# 결과를 그래프로 시각화합니다.

plt.figure(figsize=(10, 5))
plt.plot(adjusted_preds_matrix, color='blue', label='prediction')
plt.plot(test_true, color='red', label='groundtruth')
plt.title('002 1635 3746 1 ')
plt.xlabel('time')
plt.ylabel('value')
plt.axhline(0.8, color='orange', linestyle='--', label='threshold')
plt.legend()
plt.show()
plt.savefig('TEST2.png')

#path = '/Library/Fonts/NanumBarunpenR.ttf'
# path = '/usr/share/fonts/truetype/nanum/NanumSquareEB.ttf'
# font_name = fm.FontProperties(fname=path, size=1).get_name()

# #path = '/Library/Fonts/NanumBarunGothic.ttf'
# #font_name = fm.FontProperties(fname=path, size=50).get_name()

# plt.rc('font', family=font_name)
# plt.figure(figsize=(10, 5))
# plt.plot(adjusted_preds_matrix, color='blue', label='발정예측값')
# plt.plot(test_true, color='red', label='발정기록')
# plt.title('002 1361 9551 9 개체')
# plt.xlabel('시간')
# plt.ylabel('값')
# plt.axhline(0.8, color='orange', linestyle='--', label='임계점')
# plt.legend()
# plt.show()
# plt.savefig('TEST1.png')






# te = np.squeeze(test, axis=1)

# size = np.zeros(test.size)

# for i in size:
#     size[i] = i

# plt.plot(size, te)
# plt.savefig('test.png')

# TP = 0
# TN = 0
# FP = 0
# FN = 0
# for i in range((test.size-218300)):
#     pr = np.take(test, i+218300)
#     tr = np.take(test1, i+218300)
#     if pr == tr:
#         if pr == 1.0:
#             TP = TP + 1
#         else:
#             TN = TN + 1
#     else:
#         if pr == 1.0:
#             FP = FP + 1
#         else:
#             FN = FN + 1
        
# acc = (TP+TN)/(TP+TN+FP+FN)
# pre = (TP)/(TP+FP)
# recall = (TP)/(TP+FN)
# f1 = 2*(pre*recall)/(pre+recall)
        
# print(TP, TN, FP, FN)
# print(acc, recall, f1)
# print(test.size)
print(test.shape, test1.shape)
