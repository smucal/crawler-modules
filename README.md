# crawler-modules

### Setup
#### Init virtualenv
```
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3 crawler-modules
```

#### Start virtualenv
```
source crawler-modules/bin/activate
deactivate
```
#### Read and Write dependencies
```
pip3 freeze --local > requirements.txt
pip3 install -r requirements.txt
```