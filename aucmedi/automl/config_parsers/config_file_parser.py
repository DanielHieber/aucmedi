#==============================================================================#
#  Author:       Dominik Müller <= technically not :P                                              #
#  Copyright:    2024 IT-Infrastructure for Translational Medical Research,    #
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
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# Python Standard Library
import json

# Third Party Libraries
import yaml

# Internal Libraries
import aucmedi.automl.config_parsers.validation_classes as vc


#-----------------------------------------------------#
#                  Config File Parser                 #
#-----------------------------------------------------#
def parse_config_file(args, config_file_type):
    """ Internal function for parsing a YAML file to a valid configuration
    dictionary.
    """
    cmd_args = vars(args)
    config = {}

    match config_file_type:
        case "yml":
            with open(cmd_args['config_path'], 'r') as file:
                config = yaml.safe_load(file)
        case "json":
            with open(cmd_args['config_path'], 'r') as file:
                config = json.load(file)

    # validate general yaml parameters
    vc.BaseConfig(**config['general'])

    parsed_config = {}

    # validate yaml according to selected hub type
    match config['general']['hub']:
        case 'training':
            vc.TrainingConfig(**config['training'])
            parsed_config = config['training']
            if config['training']['shape_3D']:
                parsed_config['shape_3D'] = tuple(
                    config['training']['shape_3D'])
        case 'prediction':
            vc.PredictionConfig(**config['prediction'])
            parsed_config = config['prediction']
        case 'evaluation':
            vc.EvaluationConfig(**config['evaluation'])
            parsed_config = config['evaluation']

    # add general part of yaml config to parsed config
    parsed_config['hub'] = config['general']['hub']
    parsed_config['path_imagedir'] = config['general']['path_imagedir']

    return parsed_config
