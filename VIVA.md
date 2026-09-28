# Viva Questions & Answers

**1. What is Cloud Computing?**
Cloud computing is the delivery of computing services (servers, storage, databases, networking, software) over the internet ("the cloud").

**2. What is IaaS?**
Infrastructure as a Service (IaaS) provides virtualized computing resources over the internet. Example: AWS EC2.

**3. Why is AWS EC2 used in this project?**
EC2 (Elastic Compute Cloud) provides a scalable virtual machine in the cloud to host our application.

**4. What is Docker?**
Docker is a platform that uses OS-level virtualization to deliver software in packages called containers.

**5. Why use Docker?**
Docker ensures the application runs consistently across different environments by packaging the code and its dependencies together.

**6. What is Jenkins?**
Jenkins is an open-source automation server used to build, test, and deploy software (CI/CD).

**7. What is CI?**
Continuous Integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project.

**8. What is CD?**
Continuous Deployment (CD) automates the release of validated code to a repository or directly to production.

**9. What is a webhook?**
A webhook is a way for an app to provide other applications with real-time information. Here, GitHub tells Jenkins when code changes.

**10. Why use GitHub?**
GitHub provides cloud hosting for Git repositories, enabling version control and collaboration.

**11. What is Git branching?**
Branching allows developers to diverge from the main codebase to work on features or fixes independently.

**12. What happens after a GitHub push?**
The GitHub Webhook triggers Jenkins. Jenkins pulls the code, validates, builds, tests, creates a Docker image, and deploys it to the EC2 server.

**13. How is the application deployed to cloud?**
Jenkins connects to the EC2 server via SSH, pulls the new Docker image, stops the old container, and starts a new one.

**14. What is an EC2 security group?**
A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic.

**15. What is Nginx?**
Nginx is a web server that can also be used as a reverse proxy, load balancer, and HTTP cache. We use it to serve our static HTML files.

**16. Why use a cloud VM instead of a local machine?**
A cloud VM provides high availability, scalability, a public IP address for global access, and eliminates hardware maintenance.

**17. How does Jenkins communicate with the server?**
Through secure SSH (Secure Shell) using private keys stored in Jenkins Credentials.

**18. What happens if testing fails?**
The Jenkins pipeline stops immediately, marks the build as failed, and does not deploy the broken code to production.

**19. What happens if deployment fails?**
The pipeline fails, and the previous version of the application (old Docker container) remains running.

**20. Explain the complete architecture.**
Code pushed to GitHub triggers Jenkins -> Jenkins tests and builds a Docker image -> Jenkins SSH into AWS EC2 -> EC2 runs the Docker container holding Nginx -> Application is live for users.
