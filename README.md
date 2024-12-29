# network security


A simple MLOps Application for network security.


## How to Run ?

1. Create a virtual environment

```bash
conda create -p venv python==3.10 -y
```

2. Activate the environment

```bash
conda activate ./venv
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

4. Upload data to mongodb

```bash
python ./get_data.py
```

5. Install and configure aws cli
(for this step first create an IAM user and then create client id and secret with admin access and create a s3 bucket for artifact and model sync)

```bash
aws configure
```

6. Run fastapi server

```bash
python ./main.py
```


## Technology used

- Fast API
- AWS (S3, ECS, ECR)
- Github Action
- Docker and Docker compose
- Terraform
- Apache Airflow
- MongoDB
- SciKit Learn
- Numpy
- Pandas