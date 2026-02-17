import os

def file_org(files,ext):
    file_new=[file for file in files if file.endswith(ext)]
    print(file_new)
    return file_new


    

#if not(os.path.exists("images")):
    #os.mkdir("images")

    #def rename(file_new):
      #list(file_new)
def rename_process (file_new):
      a=0
      for i in file_new:
        os.rename(i,f"photo{a+1}.jpg")
        a+=1  



if __name__=="__main__":
    file=os.listdir()
    list1=file_org(file,".jpg")
    rename_process(list1)
