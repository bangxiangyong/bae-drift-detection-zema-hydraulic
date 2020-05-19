import os, requests, zipfile, io
import numpy as np
import pickle

data_url='https://zenodo.org/record/1323611/files/data.zip?download=1'

def download_and_extract(url, destination, force=False):
    response = requests.get(url)
    zipDocument = zipfile.ZipFile(io.BytesIO(response.content))
    # Attempt to see if we are going to overwrite anything
    if not force:
        abort = False
        for file in zipDocument.filelist:
            if os.path.isfile(os.path.join(destination, file.filename)):
                print(file.filename, 'already exists. If you want to overwrite the file call the method with force=True')
                abort = True
        if abort:
            print('Zip file was not extracted')
            return

    zipDocument.extractall(destination)


download_and_extract(data_url, 'dataset/ZEMA_Hydraulic/')


data_path = "dataset/ZEMA_Hydraulic/"

filenames_input_data_1Hz = ["ts1","ts2","ts3","ts4","vs1","se","ce","cp"]
filenames_input_data_1Hz = [file.upper() + ".txt" for file in filenames_input_data_1Hz]

filenames_input_data_10Hz = ["fs1","fs2"]
filenames_input_data_10Hz = [file.upper() + ".txt" for file in filenames_input_data_10Hz]

filenames_input_data_100Hz = ["ps1","ps2","ps3","ps4","ps5","ps6","eps1"]
filenames_input_data_100Hz = [file.upper() + ".txt" for file in filenames_input_data_100Hz]

data_input_data_1Hz = np.zeros((2205,60,len(filenames_input_data_1Hz)))
data_input_data_10Hz = np.zeros((2205,600,len(filenames_input_data_10Hz)))
data_input_data_100Hz = np.zeros((2205,6000,len(filenames_input_data_100Hz)))

for id_,file_name in enumerate(filenames_input_data_1Hz):
    input_data = np.loadtxt(data_path + file_name, delimiter = "\t")
    data_input_data_1Hz[:,:,id_] = input_data.copy()

for id_,file_name in enumerate(filenames_input_data_10Hz):
    input_data = np.loadtxt(data_path + file_name, delimiter = "\t")
    data_input_data_10Hz[:,:,id_] = input_data.copy()

for id_,file_name in enumerate(filenames_input_data_100Hz):
    input_data = np.loadtxt(data_path + file_name, delimiter = "\t")
    data_input_data_100Hz[:,:,id_] = input_data.copy()

filename_target_data="profile.txt"

#deal with output data now
targets_data = np.loadtxt(data_path+filename_target_data, delimiter = "\t")

#conversion of outputs to one hot
def makeOneHotVectorMap(length):
    map_toOneHot ={}
    for i in range(length):
        oneHot = np.zeros(length)
        oneHot[i] = 1
        map_toOneHot[i] = oneHot
    return map_toOneHot

id2x_dictionaries = []
x2id_dictionaries = []
id2onehot_dictionaries = []

for label in range(targets_data.shape[1]):
    label_column = list(set(targets_data[:,label]))
    label_column.sort(reverse=True)
    id2x_dictionary = {}
    x2id_dictionary = {}
    id2onehot_dictionary = makeOneHotVectorMap(len(label_column))
    for i in range(len(label_column)):
        id2x_dictionary[i] = label_column[i]
        x2id_dictionary[label_column[i]] = i
    id2x_dictionaries+=[id2x_dictionary]
    x2id_dictionaries+=[x2id_dictionary]
    id2onehot_dictionaries+=[id2onehot_dictionary]

#convert a row into one-hot coded multi-class multi-label
onehot_tensor_output = []
id_output =[]
for row in range(targets_data.shape[0]):
    row_output_data= targets_data[row]
    onehots_row =[]
    id_row =[]
    for label in range(row_output_data.shape[0]):
        id_ = x2id_dictionaries[label][row_output_data[label]]
        onehot= id2onehot_dictionaries[label][id_]
        onehots_row =np.append(onehots_row,onehot)
        id_row = np.append(id_row,id_)
    id_output+=[id_row]
    onehot_tensor_output += [onehots_row]
onehot_tensor_output = np.array(onehot_tensor_output)
id_tensor_output = np.array(id_output)

tensor_output = id_tensor_output
all_tensor_output = id_tensor_output


#save raw data into dict
raw_data = {"Hz_1":data_input_data_1Hz,
            "Hz_10":data_input_data_10Hz,
            "Hz_100":data_input_data_100Hz,"target":all_tensor_output}
#labels
print(x2id_dictionaries)

pickle_folder= "pickles"

if os.path.exists(pickle_folder) == False:
    os.mkdir(pickle_folder)

#Pickle them
pickle.dump(raw_data, open(pickle_folder+"/raw_data.p", "wb" ) )
