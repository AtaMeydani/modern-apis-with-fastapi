# Weather App

This project is a weather application built with FastAPI. It provides weather data through a RESTful API. This README outlines the steps necessary to set up and run the application on a server.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Steps](#setup-steps)
- [Running the Application](#running-the-application)
- [Setting Up NGINX](#setting-up-nginx)
- [Optional: SSL Support](#optional-ssl-support)

## Prerequisites

Before setting up the weather app, ensure that you have the following prerequisites installed on your server:
- **Python 3** (with `python3-pip`)
- **Git**
- **nginx**

## Setup Steps

Follow these steps to set up the Weather App:

1. **Install Necessary Packages**:
   ```bash
   apt-get install -y python3-pip python3-dev python3-venv
   apt-get install -y build-essential git
   apt install acl -y
   ```

2. **Create a New User for the Application**:
   ```bash
   useradd -M apiuser
   usermod -L apiuser
   ```

3. **Create the Web App File Structure**:
   ```bash
   mkdir /apps
   chmod 777 /apps
   mkdir -p /apps/logs/weather_api/app_log
   setfacl -m u:apiuser:rwx /apps/logs/weather_api
   ```

4. **Create a Virtual Environment for the App**:
   ```bash
   cd /apps
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel
   pip install --upgrade httpie glances gunicorn uvloop httptools
   ```

5. **Clone the Repository**:
   ```bash
   cd /apps
   git clone https://github.com/talkpython/modern-apis-with-fastapi app_repo
   ```

6. **Install Dependencies for the Web App**:
   ```bash
   cd /apps/app_repo/03_weather_api_project
   pip install -r requirements.txt
   ```

7. **Copy and Enable the Systemd Daemon**:
   ```bash
   cp /apps/app_repo/03_weather_api_project/service/weather.service /etc/systemd/system/
   systemctl daemon-reload
   systemctl start weather
   systemctl status weather
   systemctl enable weather
   ```

## Setting Up NGINX

1. **Install NGINX**:
   ```bash
   apt install nginx
   ```

2. **Remove the Default NGINX Configuration** (Be careful with this step):
   ```bash
   rm /etc/nginx/sites-enabled/default
   ```

3. **Copy the NGINX Configuration for the Weather App**:
   ```bash
   cp /apps/app_repo/ch08-deployment/server/nginx/weather.nginx /etc/nginx/sites-enabled/
   ```

4. **Enable NGINX to Start on Boot and Restart the Service**:
   ```bash
   update-rc.d nginx enable
   service nginx restart
   ```

## Optional: SSL Support

For enhanced security, you may want to enable SSL for your NGINX server using Let's Encrypt. For instructions, refer to the following link:
[Secure NGINX with Let's Encrypt on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)

## Conclusion

Your Weather App is now set up and running! You can access the API to retrieve weather data. For further modifications and improvements, check the project repository for more information.

