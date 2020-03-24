import numpy as np
# Deep Learning Librairies
import tensorflow as tf
import tensorflow.keras.applications as ka
import tensorflow.keras.layers as kl
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import tensorflow.keras.preprocessing.image as kpi
from tensorflow_core.python.keras.engine.network import Network

# Constants importation
import constants as cst


class Co2Inference:
    """
    Co2Inference is a class which determines tje CO2 rejection for a car in an image.
    Input: A cropped image on which a single car is visible
    Output: An array of prediction (length = class number)
    """
    WEIGHTS_PATH = "data/pretrained_weights/weights_model_ResNet50V2_fully_connected_model_5_epochs_1_batch_size.h5"

    def __init__(self):
        # due to error : failed to initialize cudnn
        self.config = ConfigProto()
        self.config.gpu_options.allow_growth = True
        self.session = InteractiveSession(config=self.config)
        self.model: Network = None
        self.init_model()

    def init_model(self, pretrained_model=ka.ResNet50V2, output_fct='relu'):
        input_tensor = tf.keras.Input(shape=cst.IMG_SHAPE)

        # create the base pre-trained model
        base_model = pretrained_model(input_tensor=input_tensor, weights='imagenet', include_top=False)

        for layer in base_model.layers:
            layer.trainable = False

        x = base_model.output
        x = kl.GlobalAveragePooling2D(data_format='channels_last')(x)
        x = kl.Dropout(0.5)(x)
        x = kl.Dense(len(cst.CAR_BODY_TYPES), activation=output_fct)(x)

        updated_model = tf.keras.Model(base_model.input, x)

        self.model = updated_model

    def summary_model(self):
        self.model.summary()

    def format_img(self, img_path):
        img = kpi.load_img(img_path).resize((cst.IMG_HEIGHT, cst.IMG_WIDTH))
        x = kpi.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        y = self.model.predict(x)

    def predict_model(self, x):
        return self.model.predict(x)

    def load_weights(self):
        self.model.load_weights(self.WEIGHTS_PATH)

    """
    Evaluate the model and returns the loss and the accuracy
    """

    def evaluate_model(self, test_images, test_labels, verbose=2):
        loss, acc = self.model.evaluate(test_images, test_labels, verbose=verbose)
        print("Restored model, accuracy: {:5.2f}%".format(100 * acc))
        return loss, acc

    def _compile_model(self):
        self.model.compile(optimizer='rmsprop',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])
