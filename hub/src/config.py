# paths
path_single = 'hub/data/dataset_single.csv'
path_multi = 'hub/data/dataset_multi.csv'

COL_TARGET_SINGLE = 'P1'
COL_TARGET_MULTI = ['P1','P2','P3','P4', 'P5', 'P6', 'P7', 'P8', 'P9']

DATASET_PATH = {'single': 'hub/data/dataset_single.csv',
                'multi': 'hub/data/dataset_multi.csv'}

MODEL_OUTPUT = {'single': 'hub/models/model_pred_single.bin',
                'multi': 'hub/models/model_pred_multi.bin'}

# Select DL model :
## model1 : A Feed Forward Neural Network. This model takes the extracted features of a molecule as input and predict the P1 property  of the dataset_single.csv dataset
## model2 : GRU model takes the smile string character as input and predict the P1 property  of the dataset_single.csv dataset
## model1_9 : Extension of Model1to predict the P1, P2,...P9 properties of the dataset_multi.csv dataset

MODEL_TYPE = 'model2'

debug = False

batch_size = 30
nb_epochs = 100
dropout_rate = 0.2
lr = 0.001
output_dim = 1
