import pandas as pd
import pickle


mdf = pd.read_excel(f"raw_files/P-00SH UBC - Vojnits Study 1 (2024-10-15).xlsx" , sheet_name='Sample Sheet',header=20 , index_col= 0)
mdf['Your Sample ID'] = mdf['Your Sample ID'].apply(lambda x: x.split("-5")[0])
mid2pid = mdf.to_dict()['Your Sample ID']

df = pd.read_excel(f"raw_files/Combined_KV_2024_NK.xlsx" , sheet_name='In the lab',header=0 , index_col= 0)
pid2sid = df.to_dict()['stool_kit_id']

meta_names = pd.read_csv("raw_files/metgenomics_files_names.txt").iloc[:,0].values.tolist()
meta_ids = list(set([x.split("_")[0] for x in meta_names]))



S_names = pd.read_csv("raw_files/16S_files_names.txt").iloc[:,0].values.tolist()
S_ids = list(set([f'P{x.split("_")[0].replace("A","")}' for x in S_names]))

with open("id_mapper.pkl",'wb') as f:
    pickle.dump([mid2pid,pid2sid, meta_ids , S_ids , meta_names , S_names],f)
