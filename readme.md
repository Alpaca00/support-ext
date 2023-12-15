### Support and reporting bugs

##### Install dependencies

```shell
pip install -r requirements.txt
```

##### Deployment to App Automate storage

```shell
curl -u "BROWSERSTACK_USERNAME:BROWSERSTACK_ACCESS_KEY" \       
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@./builds/Payload.ipa" \
-F "custom_id=ios17"
```


### ISSUES:

#### **_ticket #1047607_**

##### Add environment variables to `.env` file

```shell
BROWSERSTACK_USERNAME_REP=your_username
BROWSERSTACK_ACCESS_KEY_REP=your_access_key
```

##### Run the test

```shell
python -m unittest tests/ios_17_issue/test_ios_17_version.py
```
