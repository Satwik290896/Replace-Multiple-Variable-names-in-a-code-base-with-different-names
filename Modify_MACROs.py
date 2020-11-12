import os
import glob
import shutil 
import sys


def main():
    ML1_path = sys.argv[1]
    ML1_module = sys.argv[2]
    ML1_module_directory = ML1_path + '\\' + ML1_module
    Directory_function(ML1_module_directory) 


def Directory_function(present_dir_path):
    for curr_file_dir in os.listdir(present_dir_path):
      curr_file_dir_path = present_dir_path + '\\' + curr_file_dir
      print(curr_file_dir_path)

      if os.path.isfile(curr_file_dir_path):
        create_temp_file(present_dir_path)
        temp_file_path = present_dir_path + "\\TempCFile.txt"
        modify_temp_file(curr_file_dir_path,temp_file_path)
        write_modified_content_to_file(curr_file_dir_path,temp_file_path)
        delete_temp_file(temp_file_path)  
      else:
          Directory_function(curr_file_dir_path)
   

def create_temp_file(dir_path):
    f1 = open(dir_path + "\\TempCFile.txt", "w+")
    f1.close()

def modify_temp_file(file_path,temp_file_path):
    no_necessary_replace = int(sys.argv[3])
    with open(file_path,'r') as file_handle:
          f1 = open(temp_file_path, "w+")
          for line in file_handle:
              for i_rep in range(0,no_necessary_replace):
                line1 = line.replace(sys.argv[2*i_rep + 4],sys.argv[2*i_rep + 4 + 1])
                line = line1
              f1.write(line)
    f1.close()
    file_handle.close()


def write_modified_content_to_file(file_path,temp_file_path):
    with open(temp_file_path, "r") as f1:
          with open(file_path,'w') as file_handle:
            file_handle = open(file_path,'w')
            data = f1.read()
            file_handle.write(data)
    f1.close()
    file_handle.close()


def delete_temp_file(temp_file_path):
    os.remove(temp_file_path)


if __name__ == '__main__':
    main()