# FBU App: Places Deep Learning repository

## Table of Contents
1. [Overview](#overview)
    * [Description](#description)
2. [Important links](#links)

## Overview

### Description
While developing PlacesApp, a possibility of integrating a complex deep learning model running embedded on the app was seen, that would give the app a plus by using native android tools to run a TensorFlow Lite model.

The model is used while creating a new place. When a picture is taken of the food the place serves the picture is analyzed (in place, without any network requests), and the model provides with a category the food may form a part of.

The choosen model to integrate is a MobileNetV2 arquitecture. This because it is the lastest release from Google as the best neural network model for image classification designed specifically to run on mobile phones. As this is a image classification problem (into 5 categories), and it is going to be implemented on a mobile app, this is the perfect model to solve the problem.

The model was trainned on over 1800 images, running over 150 epochs. The results from the model can be found in this Classification Report.

![Classification Report](https://github.com/pablo-blancoc/PlacesApp-ml/blob/main/files/report.png)


This is an image of the model in action as seen from the users perspective in the app. The picture taken in this example was of a coffee container.

![Example image](https://github.com/pablo-blancoc/PlacesApp-ml/blob/main/files/example.jpeg)

## Links

[Main repository of Places App project](https://github.com/pablo-blancoc/PlacesApp)
[Backend repository of Places App](https://github.com/pablo-blancoc/PlacesApp-server)
