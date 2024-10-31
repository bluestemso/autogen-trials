import subprocess

def create_conda_env(env_name):
    subprocess.run(['conda', 'create', '-n', env_name, 'python=3.11'])  # Adjust Python version as needed
    subprocess.run(['conda', 'activate', env_name])

if __name__ == '__main__':
    repo_name = input("Enter the repository name: ")
    create_conda_env(repo_name)
