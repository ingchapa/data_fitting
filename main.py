import pandas as pd
from tqdm import tqdm
from classes.data import Variable
from classes.analyst import Analyst


#Define the batch names---------------------------------------------------------
batch_names = {'Batch 1': 'batch_1',
               'Batch 2': 'batch_2',
               'Batch 3': 'batch_3',
               'Batch 4': 'batch_4',
               'Batch 5': 'batch_5'}
#Ceate the vriables-------------------------------------------------------------
fe = Variable(var_name='Fe', path = 'data/fe.xlsx', batch_names=batch_names)
sio2 = Variable(var_name='SiO2', path = 'data/sio2.xlsx', batch_names=batch_names)
al2o3 = Variable(var_name='Al2O3', path = 'data/al2o3.xlsx', batch_names=batch_names)
p = Variable(var_name='P', path = 'data/p.xlsx', batch_names=batch_names)
mn = Variable(var_name='Mn', path = 'data/mn.xlsx', batch_names=batch_names)
h2o = Variable(var_name='H2O', path = 'data/h2o.xlsx', batch_names=batch_names)
pass015 = Variable(var_name='Passing 0.15mm', path = 'data/pass015mm.xlsx', batch_names=batch_names)
ret1 = Variable(var_name='Retained 1mm', path = 'data/ret1mm.xlsx', batch_names=batch_names)
ret6 = Variable(var_name='Retained 6.3mm', path = 'data/ret6.3mm.xlsx', batch_names=batch_names)
ret10 = Variable(var_name='Retained 10mm', path = 'data/ret10mm.xlsx', batch_names=batch_names)
#Make a list with the variables-------------------------------------------------
variables = [fe, sio2, al2o3, p, mn, h2o, pass015, ret1, ret6, ret10]
#Define the analyst-------------------------------------------------------------
analyst = Analyst()
#Define the list and fit the distributions-----------------------
var_names = ['Variable', 'Batch']
global_value_list = []
for variable in tqdm(variables, 'Fitting distributions...'):
    for batch in batch_names:
        case_list = [variable.name, batch]
        norm_fit, lognorm_fit, data_fit = analyst.fit_norm_dists(variable=variable,
                                                       batch=batch,
                                                       save_path='output/images/')
        var_list = [variable.name, batch]
        var_value_list = var_list + \
                         list(norm_fit.values()) + \
                         list(lognorm_fit.values()) + \
                         list(data_fit.values())

        column_list = var_names + \
                      list(norm_fit.keys()) + \
                      list(lognorm_fit.keys()) + \
                      list(data_fit.keys())
        global_value_list.append(var_value_list)
#Save all into a dataframe and save it as excel
output = pd.DataFrame(global_value_list, columns=column_list)
output.to_excel('output/dist_parameters.xlsx')
#analyst.lognorm_from_data(data=fe.batches['Batch 1'], mean=fe.batches['Batch 1'], cv=0.016)
