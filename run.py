import subprocess
import os

def execute(file_path):
    try:
        subprocess.run(['python', file_path], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing {file_path}:")
        print(e)

def deactivate_myenv():

    try:
        print("Successfully executed - Test Data Created")
        deactivation_script = os.path.join('myenv', 'Scripts', 'deactivate')
        deactivation_command = deactivation_script    
        subprocess.run(deactivation_command, shell=True)
        print(f"Virtual environment deactivated successfully.") 

    except subprocess.CalledProcessError as e:

        print(e)
 

if __name__ == "__main__":
    
    
    python_files = [
        'activateVirtualEnv.py',
        'workbookinitialization.py'   
    ]

    
    for file in python_files:
        execute(file)

    deactivate_myenv()   