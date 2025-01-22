import pickle

import pandas as pd

with open(f"../data/id_mapper.pkl",'rb') as f:
    mid2pid,pid2sid, meta_ids , S_ids , meta_names , S_names = pickle.load(f)


if __name__=="__main__":

    writer = pd.ExcelWriter('../data/raw_files/Combined_RK_modified.xlsx')
    find_dup = []
    for sheet_name in ['High ACE High Depression' , 'High ACE Low Depression' , 'Low ACE High Depression', 'Low ACE Low Depression']:

        df = pd.read_excel(f"../data/raw_files/Combined_KV_2024_NK_RK.xlsx", sheet_name= sheet_name , index_col=0 , header= 1)
        df = df.drop(columns=[x for x in df.columns if x not in ['stool_kit_id', 'ACE_TotalScore', 'PHQ9_Score', 'Age(yrs)', 'Sex','Race', 'Ethnicity', 'BMI', 'Negin relative ab of privotella'] ])
        df['16S_data'] = 'No'
        df['Metagenomics_data'] = 'No'
        print(sheet_name,"\t:\n")
        c , y = 0, 0
        for pid, sid  in zip(df.index , df['stool_kit_id']):
            if pid in find_dup : print(f'\n\n\n\nERROR {pid}\n\n\n\n')
            else: find_dup.append(pid)
            if sid   in S_ids:
                # print(pid, '\t', sid,'\n')
                c+=1
                df['16S_data'][pid] = 'Yes'
            if pid   in [mid2pid[x] for x in meta_ids]:
                print(pid, '\t', sid,'\n')
                y+=1
                df['Metagenomics_data'][pid] = 'Yes'
        print(f"{c} - {y} =========================================================================================================")
        df.loc['total','16S_data'] = c
        df.loc['total','Metagenomics_data'] = y
        df.to_excel(writer,sheet_name=sheet_name)
    writer.close()
