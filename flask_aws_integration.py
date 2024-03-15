import time
import boto3
from flask import Flask, jsonify

app = Flask(__name__)


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


S3_BUCKET = os.environ.get('S3_BUCKET')
S3_REGION = os.environ.get('S3_REGION')
EC2_INSTANCE_IDF = os.environ.get('EC2_INSTANCE_ID_FLASK')
EC2_INSTANCE_IDH = os.environ.get('EC2_INSTANCE_ID_HOST')
EC2_USERNAME = os.environ.get('EC2_USERNAME')



def get_ec2_instance_public_ip(instance_id):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=S3_REGION)

    # start_ec2_instance(instance_id)
    ec2_client.start_instances(InstanceIds=[instance_id])
    time.sleep(5)
    while True:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])

        try:
            state = response['Reservations'][0]['Instances'][0]['State']['Name']
            if state == 'running':
                public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
                if public_ip:
                    return public_ip
                else:
                    print("Public IP address is not available yet.")
            elif state == 'pending':
                print("Instance is still in the pending state. Waiting...")
                time.sleep(5)  # Delay for 5 seconds before checking again
            else:
                print(f"Instance is in {state} state. Unable to retrieve the public IP address.")
                return None
        except KeyError:
            print("KeyError: Unable to retrieve the public IP address.")
            print(response)  # Print the response for debugging purposes
            return None




def start_ec2_instance(instance_id):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=S3_REGION)
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    print(response)

def stop_ec2_instance(instance_id):
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=S3_REGION)
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)

@app.route('/start_instanceF', methods=['GET'])
def start_instanceF():
    start_ec2_instance(EC2_INSTANCE_IDF)
    print("EC2 instance start request sent.")
    return jsonify({'message': 'EC2 instance start request sent.'})


@app.route('/stop_instanceF', methods=['GET'])
def stop_instanceF():
    ec2_client = boto3.client('ec2',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=S3_REGION)
    ec2_client.stop_instances(InstanceIds=[EC2_INSTANCE_IDF,EC2_INSTANCE_IDH])
    return jsonify({'message': 'EC2 instance stop request sent.'})

@app.route('/get_instance_ip', methods=['GET'])
def get_instance_ip():
    public_ip = get_ec2_instance_public_ip(EC2_INSTANCE_IDF)
    if public_ip:
        return jsonify({'ip': public_ip})
    else:
        return jsonify({'message': 'Unable to retrieve the EC2 instance IP.'})

@app.route('/')
def analyse1():
    return "<p>hi there</p>"

if __name__ == '__main__':
    app.run()
