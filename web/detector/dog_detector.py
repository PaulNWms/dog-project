from keras.preprocessing import image
import keras.applications.resnet50 as resnet50
import numpy as np

app = None


def initialize_dog_detector(the_app):
    global app
    app = the_app
    app.config['RESNET_50_MODEL'] = resnet50.ResNet50(weights='imagenet')


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def predict_labels(img_path):
    global app
    model = app.config['RESNET_50_MODEL']
    # returns prediction vector for image located at img_path
    img = resnet50.preprocess_input(path_to_tensor(img_path))
    return np.argmax(model.predict(img))


def dog_detector(img_path):
    global app
    prediction = predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))
