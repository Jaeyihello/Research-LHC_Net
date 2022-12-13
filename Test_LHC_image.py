exec(open("Lib/Utils.py").read())
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array

os.environ['TF_DETERMINISTIC_OPS'] = '1'

tf.random.set_seed(0)
random.seed(0)
np.random.seed(0)


# 입력하기 전에 이미지 전처리
img_path = 'Test_Data/Images1.jpeg'
img = load_img(img_path, target_size=(224, 224)) 
 
x = img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


# MODEL IMPORT
exec(open("Lib/LHC_Net_Controller.py").read())
Params = {'num_heads': [8, 8, 7, 7, 1],
          'att_embed_dim': [196, 196, 56, 14, 25],
          'kernel_size': [3, 3, 3, 3, 3],
          'pool_size': [3, 3, 3, 3, 3],
          'norm_c': [1, 1, 1, 1, 1]}
init = [0, 0, 0, -1, -0.5]
model = LHC_ResNet34(input_shape=(224, 224, 3), num_classes=7, att_params=Params, controller_init=init)
x0 = np.ones(shape=(10, 224, 224, 3), dtype='float32')
y0 = model(x0)
model.load_weights('Downloaded_Models/LHC_NetC/LHC_Net_Controller')


#Results
print("LHC_NetC Result")
#pred_val = model.predict(validation_imagesRGB)
#perf_val = tf.keras.metrics.CategoricalAccuracy(dtype='float64')(validation_labels, pred_val).numpy()
#print('Val Perf: ', '%.17f' % perf_val)
#pred_test = model.predict(path_test)
#perf_test = tf.keras.metrics.CategoricalAccuracy(dtype='float64')(testing_labels, pred_test).numpy()
#print('result: ', pred_test)
#pred_test_uniqueness = Check_Unique(pred_test)
#print('Test Pred Repeated: ', pred_test_uniqueness)

# 이미지 분류
preds = model.predict(x)

index = -1
max_id = 0
max = preds[0][0]
for i in preds[0] :
  index  = index + 1
  if i >= max :
    max = i
    max_id = index

Categories = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
print('Predicted:', Categories[max_id])
print('Probability : ', max)



# RESET
for element in dir():
    if element[0:2] != "__":
        del globals()[element]
del element

