# CloudMonitor

CloudMonitor is an AWS EC2 monitoring project built using Python, Boto3, Docker, Amazon CloudWatch, and Amazon SNS.

## 📌 Project Overview

CloudMonitor monitors CPU utilization of an AWS EC2 instance and provides threshold-based alerts.

The Python application uses Boto3 to retrieve EC2 and CloudWatch information. The application is packaged into a Docker container and deployed on an Ubuntu EC2 instance.

Amazon CloudWatch monitors the EC2 CPU utilization, and a CloudWatch alarm triggers an Amazon SNS notification when CPU usage exceeds 70%.

## 🏗️ Architecture

```text
AWS EC2 Instance
       |
       v
Docker Container
       |
       v
Python + Boto3
       |
       v
Amazon CloudWatch
       |
       v
CloudWatch Alarm
       |
       v
Amazon SNS
       |
       v
Email Alert
```

## 🛠️ Technologies Used

* AWS EC2
* Amazon CloudWatch
* Amazon SNS
* Python
* Boto3
* Docker
* Ubuntu Linux
* Git
* GitHub

## ⚙️ How It Works

1. The application identifies the running EC2 instance.
2. Python uses Boto3 to communicate with AWS services.
3. CPU utilization is retrieved from Amazon CloudWatch.
4. The monitoring application checks the CPU utilization continuously.
5. If CPU usage exceeds 70%, the application displays a warning.
6. CloudWatch independently evaluates the configured CPU alarm.
7. When the threshold is exceeded, the CloudWatch alarm changes state.
8. Amazon SNS sends an email notification.

## 📂 Project Structure

```text
CloudMonitor/
│
├── cpu_monitor.py
├── monitor.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🐳 Docker Setup

Build the Docker image:

```bash
docker build -t cloudmonitor .
```

Run the monitoring container:

```bash
docker run -d --name cloudmonitor-app --restart unless-stopped cloudmonitor
```

Check the running container:

```bash
docker ps
```

View monitoring logs:

```bash
docker logs -f cloudmonitor-app
```

## 📊 CPU Monitoring

The Python application retrieves EC2 CPU utilization from Amazon CloudWatch using Boto3.

Example normal output:

```text
EC2 Instance: i-0dab3ec9dff6ce003
CPU Usage: 2.70%
STATUS: CPU usage is normal.
```

When CPU utilization exceeds the configured threshold:

```text
EC2 Instance: i-0dab3ec9dff6ce003
CPU Usage: 99.96%
WARNING: CPU usage is above 70%!
```

## 🚨 CloudWatch Alert Configuration

The CloudWatch alarm is configured with:

* Metric: `CPUUtilization`
* Namespace: `AWS/EC2`
* Statistic: `Average`
* Threshold: `70%`
* Evaluation period: `5 minutes`
* Notification service: Amazon SNS

## 🔔 Alert Testing

The monitoring and alerting system was tested by intentionally increasing CPU utilization on the EC2 instance.

CPU stress test:

```bash
stress --cpu 2 --timeout 300
```

During the test, the monitoring application detected CPU utilization above 70%.

The complete alert flow was verified:

```text
EC2 CPU Increase
       ↓
CloudWatch Metric
       ↓
CloudWatch Alarm
       ↓
Amazon SNS
       ↓
Email Notification
```

## ☁️ AWS Deployment

The project was deployed on an Ubuntu EC2 instance in the AWS Mumbai region (`ap-south-1`).

The monitoring application runs inside a Docker container and continuously retrieves EC2 CPU utilization from Amazon CloudWatch.

## 🎯 Key Skills Demonstrated

* AWS EC2 deployment
* Amazon CloudWatch monitoring
* CloudWatch alarm configuration
* Amazon SNS notifications
* Python and Boto3
* Docker containerization
* Linux command-line operations
* Git and GitHub
* Cloud monitoring and alerting



