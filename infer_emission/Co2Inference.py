import numpy as np
# Deep Learning Librairies
import tensorflow.keras.applications as ka
import tensorflow.keras.layers as kl
import tensorflow.keras.models as km
import tensorflow.keras.preprocessing.image as kpi
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
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

        # model initialization
        self.base_model_class = ka.InceptionResNetV2
        self.model: Network = None
        self.init_model()

        self.threshold = cst.ACC_THRESHOLD

    def init_model(self, pretrained_model=ka.ResNet50V2, output_fct='relu'):
        self._get_assembled_model(load_weights=True)

    @staticmethod
    def _get_top_model(input_shape, activation="softmax", load_weights=None):
        top_model = km.Sequential()
        top_model.add(kl.Flatten(input_shape=input_shape[1:]))
        top_model.add(kl.Dense(cst.IMG_WIDTH, activation='relu'))
        top_model.add(kl.Dropout(0.5))
        top_model.add(kl.Dense(len(cst.CAR_BODY_TYPES), activation=activation))

        if load_weights:
            top_model.load_weights(cst.path_top_model_weights)

        return top_model

    @staticmethod
    def _get_base_model(m, input_shape=cst.IMG_SHAPE):
        base_model = m(input_shape=input_shape, include_top=False, weights='imagenet')
        return base_model

    def _get_assembled_model(self, load_weights=False, load_weights_top_model=True):
        base_model = self._get_base_model(self.base_model_class)

        for layer in base_model.layers[:-1]:
            layer.trainable = False

        # get the output dimension for the base_model prediction
        img_rdn = np.random.random(cst.IMG_SHAPE)
        #     img_rdn = np.expand_dims(img_rdn, axis=0) # ajout d'une nouvelle dimension avec un 1
        img_rdn = img_rdn[np.newaxis, :, :, :]  # ajout d'une nouvelle dimension avec un None
        dim = base_model.predict(img_rdn).shape

        print("\n\n##################################")
        print("modèle utilisé : ", base_model.name)
        print("##################################\n\n")

        top_model = self._get_top_model(dim, load_weights=load_weights_top_model)
        for layer in top_model.layers[:-1]:
            layer.trainable = False

        assembled_model = km.Model(inputs=base_model.input,
                                   outputs=top_model(base_model.output),
                                   name=base_model.name + "-fine-tuned")
        if load_weights:
            assembled_model.load_weights(cst.path_assembled_weights)

        self.model = assembled_model

    def summary_model(self):
        self.model.summary()

    @staticmethod
    def format_img(img_path):
        img = kpi.load_img(img_path).resize((cst.IMG_HEIGHT, cst.IMG_WIDTH))
        x = kpi.img_to_array(img) / 255
        # x = np.expand_dims(x, axis=0)
        x = x[np.newaxis, :, :, :]
        return x

    """
    Return a list of predictions for a list of image paths.
    each prediction is an array of size=class number.
    imgs:parameter  can be:
        - a list of paths, in this case the images are loaded with pillow (PIl format) and formatted. In this case, you
        must set is_img_formatted to False (default value)
        - a list of images already formatted and in PIL format. In this case, you
        must set is_img_formatted to True
    """

    def predict(self, imgs, is_img_formatted=False):
        imgs = list(imgs)
        predictions = []

        for img_path in imgs:
            if is_img_formatted is False:
                img_formatted = self.format_img(img_path)
            else:
                img_formatted = imgs
            predictions.append(self.model.predict(img_formatted))
        print(predictions)

        return predictions

    """
    Return a list of CO2 rejection and a list of car body types detected in output for a list of img_paths in input.
    For each image, if we can't determine precisely the body type car, we chose the global average calculted with
    the car sells and the body type car rejections (source: ADEME.FR)
    """

    def get_co2(self, img_paths, is_img_formatted=False):
        predictions = self.predict(img_paths, is_img_formatted)
        rejections = []
        car_body_types = []

        for img_pred in predictions:
            # if the best prediction is under the threshold, we take the average computed
            if np.max(img_pred) < self.threshold:
                rejections.append(cst.AVERAGE_REJECTION)
                car_body_types.append(None)
            else:
                num_class = np.argmax(img_pred)
                class_name = cst.CAR_BODY_TYPES[num_class]
                car_body_types.append(class_name)
                rejection = cst.REJECTIONS[class_name]
                rejections.append(rejection)

        return rejections, car_body_types


if __name__ == '__main__':
    co2infer = Co2Inference()
    img_path = cst.path_data_train + '/cabriolet/0150.jpg'
    rejections, car_body_types = co2infer.get_co2([img_path])
    print(rejections)
    print(car_body_types)
