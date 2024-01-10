#Run with Web UI:
```
locust -f locustfile.py --host==https://mySite.com
```
##Run without Web UI:
locust -f locustfile.py --host==https://mySite.com --no-web-c 1000 -r 100

##You can run locust without the web UI - for example if you want to run it in some automated flow, like a CI server - by using the --no-web flag together with -c and -r