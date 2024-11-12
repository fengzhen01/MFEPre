import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.utils as np_utils
from tensorflow.keras import regularizers
# from tensorflow.keras.models import load_model
import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, matthews_corrcoef, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import re
import xlrd

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Conv1D, AveragePooling1D, Flatten, concatenate, Dropout


data_1 = xlrd.open_workbook('E:/Epan/MFEPre/dataset/protein_str_fea_576.xlsx')

train_1 = data_1.sheet_by_name(u'train')
traind_1 = []
for i in range(train_1.nrows):
    traind_1.append(train_1.row_values(i))
traind_1 = np.array(traind_1)
print(len(traind_1))

trainlabel = data_1.sheet_by_name(u'trainl')
train_label = []
for i in range(trainlabel.nrows):
    train_label.append(trainlabel.row_values(i))
train_label = np.array(train_label)
print(len(train_label))

test_1 = data_1.sheet_by_name(u'test')
tested_1 = []
for i in range(test_1.nrows):
    tested_1.append(test_1.row_values(i))
tested_1 = np.array(tested_1)
print(len(tested_1))


testlabel = data_1.sheet_by_name(u'testl')
test_label = []
for i in range(testlabel.nrows):
    test_label.append(testlabel.row_values(i))
test_label = np.array(test_label)
print(len(test_label))

data_2 = xlrd.open_workbook('E:/Epan/MFEPre/dataset/protbert_embeddings_1024.xlsx')

train_2 = data_2.sheet_by_name(u'train')
traind_2 = []
for i in range(train_2.nrows):
    traind_2.append(train_2.row_values(i))
traind_2 = np.array(traind_2)
print(len(traind_2))

test_2 = data_2.sheet_by_name(u'test')
tested_2 = []
for i in range(test_2.nrows):
    tested_2.append(test_2.row_values(i))
tested_2 = np.array(tested_2)
print(len(tested_2))

data_3 = xlrd.open_workbook('E:/Epan/MFEPre/dataset/graphnode_embeddings_1024.xlsx')

train_3 = data_3.sheet_by_name(u'train')
traind_3 = []
for i in range(train_3.nrows):
    traind_3.append(train_3.row_values(i))
traind_3 = np.array(traind_3)
print(len(traind_3))

test_3 = data_3.sheet_by_name(u'test')
tested_3 = []
for i in range(test_3.nrows):
    tested_3.append(test_3.row_values(i))
tested_3 = np.array(tested_2)
print(len(tested_3))

traind_1 = traind_1.reshape(-1, 576, 1)
traind_2 = np.expand_dims(traind_2, axis=-1)
traind_3 = traind_3.reshape(-1, 1024, 1)

tested_1 = tested_1.reshape(-1, 576, 1)
tested_2 = np.expand_dims(tested_2, axis=-1)
tested_3 = tested_2.reshape(-1, 1024, 1)



# channel_1，traind_1
inputs1 = Input(shape=(576, 1))
conv1_1 = Conv1D(filters=64, kernel_size=3, padding='same', activation='relu')(inputs1)
pool1_1 = AveragePooling1D(pool_size=2)(conv1_1)
flatten1_1 = Flatten()(pool1_1)

# channel_2，traind_2
inputs2 = Input(shape=(1024, 1))
conv2_1 = Conv1D(filters=64, kernel_size=3, padding='same', activation='relu')(inputs2)
pool2_1 = AveragePooling1D(pool_size=2)(conv2_1)
flatten2_1 = Flatten()(pool2_1)

# channel_3，traind_3
inputs3 = Input(shape=(1024, 1))
conv3_1 = Conv1D(filters=64, kernel_size=3, padding='same', activation='relu')(inputs3)
pool3_1 = AveragePooling1D(pool_size=2)(conv3_1)
flatten3_1 = Flatten()(pool3_1)

# FC_layers
merged = concatenate([flatten1_1, flatten2_1, flatten3_1])

# FC Layers
dense1 = Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01))(merged)
dense_drop1 = Dropout(0.3)(dense1)
dense2 = Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.05))(dense_drop1)
dense3 = Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.05))(dense2)
dense_drop2 = Dropout(0.3)(dense3)
outputs = Dense(2, activation='softmax')(dense_drop2)


model = Model(inputs=[inputs1, inputs2, inputs3], outputs=outputs)


model.summary()


model.compile(loss="categorical_crossentropy",
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              metrics=["accuracy"])    # 编译模型，设置损失函数和优化器


history = model.fit([traind_1, traind_2, traind_3],
                    train_label,
                    epochs=30, batch_size=500, shuffle=True)


y_pred_prob = model.predict([tested_1, tested_2, tested_3])
y_pred = np.argmax(y_pred_prob, axis=1)
y_true = np.argmax(test_label, axis=1)

conf_matrix = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(conf_matrix)


test_accuracy = np.sum(y_pred == y_true) / len(y_true)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
mcc = matthews_corrcoef(y_true, y_pred)

# AUC
fpr, tpr, _ = roc_curve(y_true, y_pred_prob[:, 0])
auc_score = roc_auc_score(y_true, y_pred_prob[:, 0])


print("Test Accuracy: {:.4f}".format(test_accuracy))
print("Precision: {:.4f}".format(precision))
print("Recall: {:.4f}".format(recall))
print("F1 Score: {:.4f}".format(f1))
print("MCC: {:.4f}".format(mcc))
print("AUC: {:.4f}".format(auc_score))

# 绘制 ROC 曲线
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc_score)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()