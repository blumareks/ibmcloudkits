# ibmcloudkits
small code examples on connecting to backend services in IBM Cloud in Python

Flask hosts RESTFul API to connect to particular service

## databases for postgresql

add required env variables when starting a container:  --env-file /.../.env



`.env`:
```
HOST="hostname.databases.appdomain.cloud"
PORT= 31525
USER="username"
PASSWORD="password"
SSLMODE="verify-full"
SSLROOTCERT="/path/to/cert/ca-certificate.crt"
DATABASE="ibmclouddb"
SENDGRID_API_KEY=your-api-key
SENDGRID_FROM=your@email.com
```

https://github.com/IBM/cloud-databases-python-sdk

# ibmcloudkits
small code examples on connecting to backend services in IBM Cloud in Python
Flask hosts RESTFul API to connect to particular service


## sendGrid

set API Key in .env file
start the server
`flask run --host=0.0.0.0 --port=8000` or 
```sh

podman image build . -t <your docker id>/kitsqlpy:0.3.0
podman run -p 8000:8000 --name kitsqlpy --env-file /path/to/file/env   <your docker id>/kitsqlpy:0.3.0
FYI -d for deattached running of a container
```

call: http://127.0.0.1:8000/mailtest?email=yourTo@emai.com 

## databases for postgresql

add required env variables when starting a container:  --env-file /.../.env



`.env`:
```
HOST="hostname.databases.appdomain.cloud"
PORT= 31525
USER="username"
PASSWORD="password"
SSLMODE="verify-full"
SSLROOTCERT="/path/to/cert/ca-certificate.crt"
DATABASE="ibmclouddb"
```

https://github.com/IBM/cloud-databases-python-sdk


Service Credentials from IBM Cloud:
```JSON
{
  "connection": {
    "cli": {
      "arguments": [
        [
          "host= port= dbname= user= sslmode="
        ]
      ],
      "bin": "psql",
      "certificate": {
        "certificate_authority": "self_signed",
        "certificate_base64": ,
        "name": 
      },
      "composed": [
        
      ],
      "environment": {
        "PGPASSWORD":,
        "PGSSLROOTCERT": 
      },
      "type": "cli"
    },
    "postgres": {
      "authentication": {
        "method": "direct",
        "password": ,
        "username": 
      },
      "certificate": {
        "certificate_authority": "self_signed",
        "certificate_base64": 
      },
      "composed": [
        "postgres://"
      ],
      "database": "ibmclouddb",
      "hosts": [
        {
          "hostname":,
          "port": 
        }
      ],
      "path": "/ibmclouddb",
      "query_options": {
        "sslmode": "verify-full"
      },
      "scheme": "postgres",
      "type": "uri"
    }
  },
  "instance_administration_api": {
    "deployment_id": ,
    "instance_id": ,
    "root": 
  }
}

```



```
import psycopg2

try:
    conn = psycopg2.connect(
      host="hostname.databases.appdomain.cloud",
      port= 31525,
      user="username",
      password="password",
      sslmode="verify-full",
      sslrootcert="/path/to/cert/ca-certificate.crt",
      database="ibmclouddb")
except: 
    print("Unable to connect to database")

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database")
rows = cur.fetchall()

print("List of databases:")
for row in rows:
    print("  ",row[0])

```
