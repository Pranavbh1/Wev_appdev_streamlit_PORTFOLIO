# Web Application Development using Python Programming Language
# By using STREAMLIT
* Basic setup :
   1. Creation of Virtual Environment :
      > python -m venv name_of env

   2. Activating the Virtual environment :
      > name_of_venv\Scripts\activate            #Deactivate

   3. Install Streamlit :
      >(venv)>pip install streamlit

   4. Create the Project_name folder and App.py(File which used to run all the other files in Project_name folder)
      >VScode

   5. Run your application :
      >(venv)>streamlit run App.py

   6. (To check ) All Modules of python (Dependencies installed on system)
      > pip list


# cmd Commands :
    cd
    1. cd --> Change Directory
    2. cd 'PATH' --> in order to change directory
    3. cd..  --> Take 1 directory(folder) back
    4. cd.  --> Keeps you on current Directory

# dir commands :
    1. dir --> lists down all the files/folders in current directory

# python -V  (To check the version of python installed in your system

# pip list --> Shows you all the python packages installed on your system (if you type 'pip list' in activated environment it will you all the packages installed on your virtual environment)

# Creation of Virtual Environment : 
    1. python -m venv Name_of_virtual_environment(ex:- env_portfolio)
    
# Activation of Virtual Environment :
    1. Name_of_virtual_environment\Scripts\activate

# DeActivation of Virtual Environment :
    1. Name_of_virtual_environment\Scripts\deactivate

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Error( With solution) :
   Error :- 'Python' is not recognised as internal................
   
   Reason :- Python is not set as the environment variable
   
   Soluton :- Go to loacation of folder of python installed in your system :
   
              Copy : absolute path of 'python' and 'Scripts' folder
   
              Open : Control Panel --> Edit the system environment Variables
              
              Open : Environment Variables ( in Edit the system environment Variables)
              
              Select : PATH (variable in both boxes --> GO TO Edit --> Go TO New --> Paste the copied both Absolute path.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# About Project : - 
 A. On system:
   1. Make a Folder on Desktop
   2. cmd
   3. pip install streamlit
   4. create env virtually
   5. to check python installed in virtual_env --> python -V
   6. Now install streamlit in your virtual_env by --> pip install streamlit
   7. pip list ( Optional - to check list )
   8. To check streamlit is working properly (type) --> streamlit hello

B. On Vs code :
   1. Open the folder you made (folder_name)
   2. Now , create a file having Extension.py ( ex : - App.py) ( This will help in running your created folder including files)
   3. Now , in App.py :-
         Code :- import streamlit as st
         Code :- Whatever you want ( ex:- st.title())

C. Now :
   1. Open cmd (shortcut :- ctrl+tilde(`))
   2. Change Powershell to cmd
   3. Activate env
   4. Go to Folder containing your Project
   5. dir(Optional)
   6. Type --> streamlit run App.py --> Hit Enter
      You will get local host web in your browser now if you want to share it to anyone copy your network URL : http:192.168.1...... , send it and ask to open this URL in browser ( it will Open ONLY IF YOU ARE CONNECTED WITH SAME NETWORK - LOCAL NETWORK (WIFI) .
      If you Deploy this Project on cloud anyone in the world can see it .
    
  
