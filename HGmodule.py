import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import ReduceLROnPlateau
from time import perf_counter
import cv2
import matplotlib.pyplot as plt


class HGmodule():
    def __init__(self):
        self.model = Sequential([Conv2D(filters=32, kernel_size=(3, 3), activation="relu", input_shape=(40, 40, 1)),
                            MaxPool2D(2, 2, padding='same'),

                            Conv2D(filters=128, kernel_size=(3, 3), activation="relu"),
                            MaxPool2D(2, 2, padding='same'),

                            Conv2D(filters=512, kernel_size=(3, 3), activation="relu"),
                            MaxPool2D(2, 2, padding='same'),

                            Flatten(),

                            Dense(units=1024, activation="relu"),
                            Dense(units=256, activation="relu"),
                            Dropout(0.5),
                            Dense(units=25, activation="softmax")
                            ])

        self.model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        self.model.load_weights('HGR_test_7.h5')

    def plot_image2(self,img):
        img_cvt = img
        print(img_cvt.shape)  # Prints the shape of the image just to check
        plt.imshow(img_cvt)  # Shows the image
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.show()
    def predictGesture(self, image):
        labelList = ["background","1 figure", " 2 figure", "3 figure"]
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image=cv2.resize(image,(40,40),interpolation=cv2.INTER_AREA)
        cv2.imshow("predict image",image)
        image=np.array(image)
        images = image.reshape(1, 40, 40, 1)
        classes = self.model.predict(images)
        predicted_label = np.argmax(classes)
        return labelList[predicted_label]