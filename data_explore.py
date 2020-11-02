import pickle
import os
#assumes train.cpkl is placed in a local directory 'data'.
train_data_file = os.path.join('./data/','train.cpkl')   
train_list, train_data = pickle.load(open(train_data_file,'rb'),encoding='latin1')
print('No of molecules in Training = ', len(train_data))
molecule_pair = train_data[0]
print(molecule_pair.keys())

print("l_vertex = [%d,%d]"%(molecule_pair['l_vertex'].shape))
print("l_edge = [%d,%d,%d]"%(molecule_pair['l_edge'].shape))
print("l_hood_indices = [%d,%d,%d]"%(molecule_pair['l_hood_indices'].shape))

print('--------------------------------------------------')

print("r_vertex = [%d,%d]"%(molecule_pair['r_vertex'].shape))
print("r_edge = [%d,%d,%d]"%(molecule_pair['r_edge'].shape))
print("r_hood_indices = [%d,%d,%d]"%(molecule_pair['r_hood_indices'].shape))

print('--------------------------------------------------')

print("label = [%d,%d]"%(molecule_pair['label'].shape))
print(molecule_pair['label'][0:5,:])

print('--------------------------------------------------')
