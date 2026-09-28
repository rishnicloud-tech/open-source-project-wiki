# Cloud Deployment Guide

This guide explains how to deploy the Open Source Project Wiki to AWS EC2.

## Cloud Architecture
The application runs inside a Docker container (Nginx) hosted on an AWS EC2 virtual machine.

## AWS EC2 Setup
1. Log in to the AWS Management Console.
2. Go to **EC2** and click **Launch Instance**.
3. Name: `Wiki-Server`.
4. AMI: **Ubuntu Server 22.04 LTS**.
5. Instance Type: **t2.micro** (Free Tier eligible).
6. Key Pair: Create a new key pair (`wiki-key.pem`) and download it.
7. Click **Launch Instance**.

## Security Group Setup
1. In the EC2 console, go to **Security Groups**.
2. Edit the inbound rules for the instance's security group.
3. Add Rule: Type = **SSH**, Port = **22**, Source = **My IP** (or Anywhere for testing).
4. Add Rule: Type = **HTTP**, Port = **80**, Source = **Anywhere-IPv4**.

## SSH Connection
Connect to the server using the downloaded key pair:
```bash
ssh -i wiki-key.pem ubuntu@<YOUR_EC2_PUBLIC_IP>
```

## Docker Installation (on EC2)
Run the following commands on the EC2 instance:
```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```
Log out and log back in to apply docker group permissions.

## Application Deployment (Manual)
1. Clone the repository on the EC2 instance:
   ```bash
   git clone <YOUR_GITHUB_REPOSITORY>
   cd open-source-project-wiki
   ```
2. Build the app (if node/npm is used, else skip):
   ```bash
   bash scripts/build.sh
   ```
3. Build the Docker image:
   ```bash
   docker build -t wiki-app .
   ```
4. Run the Docker container:
   ```bash
   docker run -d -p 80:80 --name wiki-container wiki-app
   ```

## Jenkins Integration (Automated Deployment)
1. Add the EC2 Public IP and SSH Key as **Credentials** in Jenkins.
2. The Jenkins pipeline uses SSH to connect to the EC2 instance, pulls the latest code/image, stops the old container, and starts the new one automatically.

## Public IP Access
Open a web browser and navigate to:
```
http://<YOUR_EC2_PUBLIC_IP>
```

## Troubleshooting
- **Cannot connect via SSH:** Ensure Port 22 is open in the Security Group and you are using the correct key.
- **Website not loading:** Ensure Port 80 is open in the Security Group and the Docker container is running (`docker ps`).
- **Check container logs:** `docker logs wiki-container`

## Stop/Start Commands
- Stop container: `docker stop wiki-container`
- Start container: `docker start wiki-container`
- Restart container: `docker restart wiki-container`
