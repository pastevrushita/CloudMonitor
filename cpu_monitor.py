import boto3
from datetime import datetime, timedelta, timezone

REGION = "ap-south-1"

ec2 = boto3.client("ec2", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)

instances = ec2.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running"]}
    ]
)

instance_id = instances["Reservations"][0]["Instances"][0]["InstanceId"]

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(minutes=5)

response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[
        {
            "Name": "InstanceId",
            "Value": instance_id
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average"]
)

print("EC2 Instance:", instance_id)

if response["Datapoints"]:
    latest = sorted(
        response["Datapoints"],
        key=lambda x: x["Timestamp"]
    )[-1]

    cpu = latest["Average"]

    print(f"CPU Usage: {cpu:.2f}%")

    if cpu > 70:
        print("WARNING: CPU usage is above 70%!")
    else:
        print("STATUS: CPU usage is normal.")
else:
    print("No CPU data available yet.")
