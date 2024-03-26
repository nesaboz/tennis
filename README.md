## Setup EC2 instance for training

Install "Remote Development" locally

Connect to machine Commnad+Shift+P, "Remote SSH ...", "Connect to host", 
then `ssh -i <path to pem file> ubuntu@<ip address>`

Then "Python" and "Jupyter" extensions in VSCode on a remote machine.

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3.10-venv
sudo apt-get install -y libgl1-mesa-glx
python3 -m venv venv
source venv/bin/activate
pip install jupyter notebook ipykernel
python -m ipykernel install --user --name=tennis --display-name "tennis"
pip install ultralytics roboflow python-dotenv
```

To install Python:
```bash
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
whereis python3.8
sudo apt install -y python3.8-venv
/usr/bin/python3.8 -m venv venv
```

git config --global user.email "nesaboz@gmail.com"
git config --global user.name "Nenad Bozinovic"