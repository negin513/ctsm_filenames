import pandas as pd
import os
import glob

def read_name_table ( table_name):
    """
    Assuming we have a correct name_table
    Read all the columns of name_table
    Recursively list all the files in a directory
    Returns All dir_name , old_name, new_name in a df
    """
    df = pd.read_csv(table_name)

    return df
    #dir_names = []
    #fnames    = []
    #for this_file in glob.iglob(dir + '**/*.F90', recursive=True):
    #         this_dir    =  os.path.dirname(this_file)
    #         this_fname  =  os.path.basename(this_file)
    #         dir_names.append(this_dir)
    #         fnames.append(this_fname)

    #df               = pd.DataFrame()
    #df['dir_name']   = dir_names
    #df['old_fname']  = fnames

    #print ("df=list_files(dir)")
    #print (df)
    #print ("==================")

    return df; 


def create_new_name (old_fname):
    # add ctsm_ to fname and capitilize the first letter
    new_fname = 'ctsm_'+old_fname[0].upper() +old_fname[1:]
    # remove Mod 
    new_fname = new_fname.replace("Mod","")
    #print ('~~~ new_fname for ', old_fname, 'is', new_fname , '~~~')
    return new_fname;

def name_table (all_files):
    """
    go over all names df and create a table df including:
    dir_name old_name new_name old_string new_string
    """
    df_out     = pd.DataFrame(columns=['dir_name', 'old_fname', 'new_fname', 'old_string', 'new_string'])

    for index, row in all_files.iterrows():
        old_fname            =  row['old_fname']
        new_fname            =  create_new_name (old_fname)
        old_string           =  old_fname.replace(".F90","")
        new_string           =  new_fname.replace(".F90","")
        row ['new_fname']    =  new_fname
        row ['old_string']   =  old_string
        row ['new_string']   =  new_string
        df_out               =  df_out.append(row)
    return df_out;


def main():

    tmp_data = read_name_table ('../ctsm_filenames.csv')
    
    dir_names = []
    old_fname =[]
    new_fname =[]


    dir_names = tmp_data['dir_name']
    old_fname = tmp_data['old_fname']
    new_fname = tmp_data['new_fname']

    length = len(dir_names) 

    for i in range (length):
        if os.path.exists(dir_names[i]+'/'+old_fname[i]):
            print (dir_names[i]+old_fname[i], ' exists!')
            #os.rename (dir_names[i]+old_fname[i], dir_names[i]+new_fname[i])
            print (dir_names[i]+'/'+old_fname[i],' is changed to ', dir_names[i]+'/'+new_fname[i])
        else:
            print (dir_names[i]+old_fname[i], ' does NOT exist!')

if __name__ == "__main__":
    main()



"""
    base_dir   =  "/glade/scratch/negins/ctsm_0110/src/"
    all_files  =  list_files(base_dir)
    table_out  =  name_table (all_files)

    table_out.to_csv('ctsm_names.csv', sep='\t', encoding='utf-8')
"""
