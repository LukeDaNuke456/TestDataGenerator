import os
import sys
import subprocess

env_created = False

def check_os():
    os_name = os.name
    
    if os_name == 'posix':
        return "Unix/Linux/Mac OS X"
    
    elif os_name == 'nt':
        return "Windows"
    
    else:
        return "Unknown Operating System"


def create_virtual_enviornment():
    os_type = check_os()
    print("Operating System detected:", os_type)
    
    if not os.path.exists(env_filename):
    
        if os_type == "Unix/Linux/Mac OS X":
            try: 
                subprocess.run([sys.executable, '-m', 'venv', 'myenv'])
                print("Virtual environment 'myenv' created successfully.")
            except Exception as e:
                print(f"Error occurred while creating virtual environment: {e}")
        elif os_type == "Windows":  
            try:
                subprocess.run([sys.executable, '-m', 'venv', 'myenv'], shell=True)
                print("Virtual environment 'myenv' created successfully.")
                env_created = True
            except Exception as e:
                print(f"Error occurred while creating virtual environment: {e}")
        else:
            print("Virtual environment creation is not supported on this operating system.")

        if env_created: 

            activate_env()
                
            
    elif os.path.exists(env_filename):

        print ("myenv already exists!")
        activate_env()
        
    else:
        print("Virtual environment creation failed")


def activate_env():

    try:
        activation_script = os.path.join('myenv', 'Scripts', 'activate.bat')
        activation_command = activation_script    
        subprocess.run(activation_command, shell=True)
        print(f"Virtual environment activated successfully.")
            
    except Exception as e:
        print(f"Error occurred while activating virtual environment: {e}")
        print(f"Run the following command to activate the virtual environment:\n{activation_command}")
    

def install_packages(package_name):

    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', package_name], check=True)
        print(f"Package '{package_name}' installed successfully.")
    except Exception as e:
        print(f"Error occurred while installing package '{package_name}': {e}")    


if __name__ == "__main__":

    env_filename = 'myenv'
    package_name = 'openpyxl'
    create_virtual_enviornment() 
    install_packages(package_name)

 

