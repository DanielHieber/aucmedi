#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
# Abstract Base Class for Architectures
from aucmedi.neural_network.architectures.arch_base import Architecture_Base

#-----------------------------------------------------#
#                    Architectures                    #
#-----------------------------------------------------#
# Vanilla Classifier
from aucmedi.neural_network.architectures.volume.vanilla import Architecture_Vanilla
# DenseNet
from aucmedi.neural_network.architectures.volume.densenet121 import Architecture_DenseNet121
from aucmedi.neural_network.architectures.volume.densenet169 import Architecture_DenseNet169
from aucmedi.neural_network.architectures.volume.densenet201 import Architecture_DenseNet201
# ResNet
from aucmedi.neural_network.architectures.volume.resnet18 import Architecture_ResNet18
from aucmedi.neural_network.architectures.volume.resnet34 import Architecture_ResNet34
from aucmedi.neural_network.architectures.volume.resnet50 import Architecture_ResNet50
from aucmedi.neural_network.architectures.volume.resnet101 import Architecture_ResNet101
from aucmedi.neural_network.architectures.volume.resnet152 import Architecture_ResNet152
# ResNeXt
from aucmedi.neural_network.architectures.volume.resnext50 import Architecture_ResNeXt50
from aucmedi.neural_network.architectures.volume.resnext101 import Architecture_ResNeXt101
# MobileNet
from aucmedi.neural_network.architectures.volume.mobilenet import Architecture_MobileNet
from aucmedi.neural_network.architectures.volume.mobilenetv2 import Architecture_MobileNetV2
# VGG
from aucmedi.neural_network.architectures.volume.vgg16 import Architecture_VGG16
from aucmedi.neural_network.architectures.volume.vgg19 import Architecture_VGG19

#-----------------------------------------------------#
#       Access Functions to Architecture Classes      #
#-----------------------------------------------------#
# Architecture Dictionary
architecture_dict = {
    "Vanilla": Architecture_Vanilla,
    "DenseNet121": Architecture_DenseNet121,
    "DenseNet169": Architecture_DenseNet169,
    "DenseNet201": Architecture_DenseNet201,
    "ResNet18": Architecture_ResNet18,
    "ResNet34": Architecture_ResNet34,
    "ResNet50": Architecture_ResNet50,
    "ResNet101": Architecture_ResNet101,
    "ResNet152": Architecture_ResNet152,
    "ResNeXt50": Architecture_ResNeXt50,
    "ResNeXt101": Architecture_ResNeXt101,
    "MobileNet": Architecture_MobileNet,
    "MobileNetV2": Architecture_MobileNetV2,
    "VGG16": Architecture_VGG16,
    "VGG19": Architecture_VGG19,
}
""" Dictionary of implemented 3D Architectures Methods in AUCMEDI.

    The base key (str) or an initialized Architecture can be passed to the [Neural_Network][aucmedi.neural_network.model.Neural_Network] class as `architecture` parameter.

    ???+ example "Example"
        ```python title="Recommended via Neural_Network class"
        my_model = Neural_Network(n_labels=4, channels=1, architecture="3D.ResNet50")
        ```

        ```python title="Manual via architecture_dict import"
        from aucmedi.neural_network.architectures import architecture_dict
        my_arch = architecture_dict["3D.ResNet50"](channels=1, input_shape=(128,128,128))
        my_model = Neural_Network(n_labels=4, channels=1, architecture=my_arch)
        ```

    ???+ warning
        If passing an architecture key to the Neural_Network class, be aware that you have to add "3D." infront of it.

        For example:
        ```python
        # for the volume architecture "ResNeXt101"
        architecture="3D.ResNeXt101"
        ```

    Architectures are based on the abstract base class [aucmedi.neural_network.architectures.arch_base.Architecture_Base][].
"""

# List of implemented architectures
architectures = list(architecture_dict.keys())

#-----------------------------------------------------#
#       Meta Information of Architecture Classes      #
#-----------------------------------------------------#
# Utilized standardize mode of architectures required for Transfer Learning
supported_standardize_mode = {
    "Vanilla": "z-score",
    "DenseNet121": "torch",
    "DenseNet169": "torch",
    "DenseNet201": "torch",
    "ResNet18": "grayscale",
    "ResNet34": "grayscale",
    "ResNet50": "grayscale",
    "ResNet101": "grayscale",
    "ResNet152": "grayscale",
    "ResNeXt50": "grayscale",
    "ResNeXt101": "grayscale",
    "MobileNet": "tf",
    "MobileNetV2": "tf",
    "VGG16": "caffe",
    "VGG19": "caffe",
}
""" Dictionary of recommended [Standardize][aucmedi.data_processing.subfunctions.standardize] techniques for 3D Architectures Methods in AUCMEDI.

    The base key (str) can be passed to the [DataGenerator][aucmedi.data_processing.data_generator.DataGenerator] as `standardize_mode` parameter.

    ???+ info
        If training a new model from scratch, any Standardize technique can be used at will. <br>
        However, if training via transfer learning, it is required to use the recommended Standardize technique!

    ???+ example "Example"
        ```python title="Recommended via the Neural_Network class"
        my_model = Neural_Network(n_labels=8, channels=3, architecture="3D.DenseNet121")

        my_dg = DataGenerator(samples, "images_dir/", labels=None,
                              resize=my_model.meta_input,                  # (64, 64, 64)
                              standardize_mode=my_model.meta_standardize)  # "torch"
        ```

        ```python title="Manual via supported_standardize_mode import"
        from aucmedi.neural_network.architectures import supported_standardize_mode
        sf_norm = supported_standardize_mode["3D.DenseNet121"]
        my_dg = DataGenerator(samples, "images_dir/", labels=None,
                              resize=(64, 64, 64),                         # (64, 64, 64)
                              standardize_mode=sf_norm)                    # "torch"
        ```

    ???+ warning
        If using an architecture key for the supported_standardize_mode dictionary, be aware that you have to add "3D." infront of it.

        For example:
        ```python
        # for the volume architecture "ResNeXt101"
        from aucmedi.neural_network.architectures import supported_standardize_mode
        sf_norm = supported_standardize_mode["3D.ResNeXt101"]
        ```
"""
