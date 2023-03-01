import os

# Replace this with the URL of the repository you want to clone
repo_url = "https://github.com/Charlie-sans/Open-NBS-VR.git"

# Get the current directory (where this script is located)
current_dir = os.getcwd()

# Extract the name of the repository from the URL
repo_name = repo_url.split("/")[-1].split(".")[0]

# Create a path for the new directory where the repository will be cloned
new_dir = os.path.join(current_dir, repo_name)

if not os.path.isdir(new_dir):
    # Use the git command line tool to clone the repository
    os.system(f"git clone {repo_url} {new_dir}")
else:
    # Use the git command line tool to check for changes in the repository
    os.chdir(new_dir)
    os.system("git fetch")
    result = os.system("git diff HEAD origin/master --name-only")
    if result != 0:
        os.system("git pull")
