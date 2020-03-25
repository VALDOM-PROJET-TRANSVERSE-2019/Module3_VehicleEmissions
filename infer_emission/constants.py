# List of possible car body types
CAR_BODY_TYPES = ['berline', 'break', 'cabriolet', 'combispace', 'coupe', 'minibus', 'minispace', 'monospace',
                  'monospace compact', 'tous-terrains']

REJECTIONS = {'berline': 105.00,
              'break': 109.00,
              'cabriolet': 135.00,
              'combispace': 116.00,
              'coupe': 172.00,
              'minibus': 146.00,
              'minispace': 126.00,
              'monospace': 132.00,
              'monospace compact': 141.00,
              'tous-terrains': 119.00}

SELLS = {'berline': 49.43,
              'break': 4.18,
              'cabriolet': 0.51,
              'combispace': 2.00,
              'coupe': 0.46,
              'minibus': 0.69,
              'minispace': 0.15,
              'monospace': 0.44,
              'monospace compact': 3.84,
              'tous-terrains': 38.29}

# Threshold under which we take the global rejection average
ACC_THRESHOLD = 0.5
# The rejection average computed from ADEME.FR dataset (sells and rejections for each body type)
AVERAGE_REJECTION = 113

# Image shapes for neural network
IMG_WIDTH = 150
IMG_HEIGHT = 150
IMG_SHAPE = (IMG_WIDTH, IMG_HEIGHT, 3)

# Data paths
path_root = "../data"
path_data = path_root + '/vehicle_images'  # data path
path_data_train = path_data + '/train'
path_data_val = path_data + '/val'

# Saved objects path
path_pretrained_weights_data = path_root + "/pretrained_weights"
path_pretrained_features = path_root + "/pretrained_features"

path_assembled_weights = path_pretrained_weights_data + '/assembled_model_weights'
path_top_model_weights = path_pretrained_weights_data + '/top_model_weights'