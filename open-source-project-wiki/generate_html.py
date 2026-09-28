import os

project_dir = r'C:\Users\rishn\.gemini\antigravity\scratch\open-source-project-wiki'

# HTML Layout Template
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Open Source Project Wiki</title>
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
    <header class="main-header">
        <div class="container">
            <h1>Open Source Project Wiki</h1>
            <button id="menu-btn" class="menu-btn">&#9776;</button>
        </div>
    </header>

    <div class="container layout">
        <aside class="sidebar" id="sidebar">
            <input type="text" id="search-input" placeholder="Search documentation...">
            <nav>
                <ul id="nav-list">
                    <li><a href="{base_path}index.html">Home</a></li>
                    <li><a href="{base_path}pages/about.html">About Open Source</a></li>
                    <li><a href="{base_path}pages/getting-started.html">Getting Started</a></li>
                    <li><a href="{base_path}pages/git-github.html">Git & GitHub</a></li>
                    <li><a href="{base_path}pages/contribution.html">Contribution Guide</a></li>
                    <li><a href="{base_path}pages/pull-requests.html">Pull Requests</a></li>
                    <li><a href="{base_path}pages/issues.html">Issue Tracking</a></li>
                    <li><a href="{base_path}pages/devops.html">DevOps & CI/CD</a></li>
                    <li><a href="{base_path}pages/jenkins.html">Jenkins</a></li>
                    <li><a href="{base_path}pages/docker.html">Docker</a></li>
                    <li><a href="{base_path}pages/cloud-computing.html">Cloud Computing</a></li>
                    <li><a href="{base_path}pages/aws-deployment.html">AWS Deployment</a></li>
                    <li><a href="{base_path}pages/faq.html">FAQ</a></li>
                </ul>
            </nav>
        </aside>

        <main class="content">
            {content}
        </main>
    </div>

    <footer>
        <p>&copy; 2024 Open Source Project Wiki</p>
    </footer>

    <script src="{js_path}"></script>
</body>
</html>
'''

files = {
    'index.html': {
        'title': 'Home',
        'base_path': '',
        'css_path': 'css/style.css',
        'js_path': 'js/script.js',
        'content': '''<h2>Welcome to the Open Source Project Wiki</h2>
<p>This wiki is a comprehensive guide to understanding Open Source software development, version control, DevOps practices, and Cloud Computing deployments.</p>
<p>Navigate through the sidebar to learn about various topics.</p>'''
    },
    'pages/about.html': {
        'title': 'About Open Source', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>About Open Source</h2><p>Open source software is software with source code that anyone can inspect, modify, and enhance.</p>'''
    },
    'pages/getting-started.html': {
        'title': 'Getting Started', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Getting Started</h2><p>To get started, you will need to set up your local development environment.</p>'''
    },
    'pages/git-github.html': {
        'title': 'Git & GitHub', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Git & GitHub</h2><p>Git is a version control system. GitHub is a hosting platform for Git repositories.</p>'''
    },
    'pages/contribution.html': {
        'title': 'Contribution Guide', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Contribution Guide</h2><p>Follow these guidelines to contribute to the project.</p>'''
    },
    'pages/pull-requests.html': {
        'title': 'Pull Requests', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Pull Requests</h2><p>A Pull Request (PR) is a way to propose changes to a repository.</p>'''
    },
    'pages/issues.html': {
        'title': 'Issue Tracking', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Issue Tracking</h2><p>Use GitHub Issues to track bugs and feature requests.</p>'''
    },
    'pages/devops.html': {
        'title': 'DevOps & CI/CD', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>DevOps & CI/CD</h2><p>Continuous Integration and Continuous Deployment (CI/CD) automates software delivery.</p>'''
    },
    'pages/jenkins.html': {
        'title': 'Jenkins', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Jenkins</h2><p>Jenkins is an open source automation server.</p>'''
    },
    'pages/docker.html': {
        'title': 'Docker', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Docker</h2><p>Docker is a platform for developing, shipping, and running applications in containers.</p>'''
    },
    'pages/cloud-computing.html': {
        'title': 'Cloud Computing', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>Cloud Computing</h2>
<h3>What is Cloud Computing?</h3>
<p>Cloud computing is the on-demand delivery of IT resources over the Internet.</p>
<ul>
    <li><b>IaaS:</b> Infrastructure as a Service</li>
    <li><b>PaaS:</b> Platform as a Service</li>
    <li><b>SaaS:</b> Software as a Service</li>
</ul>
<h3>Virtual Machines</h3>
<p>VMs are emulations of computer systems providing cloud compute.</p>'''
    },
    'pages/aws-deployment.html': {
        'title': 'AWS Deployment', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>AWS Deployment</h2>
<ol>
    <li>Create AWS account</li>
    <li>Launch EC2 instance (Ubuntu)</li>
    <li>Configure Security Group (Port 22, 80)</li>
    <li>SSH into instance: <code>ssh -i YOUR_SSH_KEY ubuntu@YOUR_EC2_PUBLIC_IP</code></li>
    <li>Install Docker</li>
    <li>Clone repository</li>
    <li>Run Docker container</li>
</ol>'''
    },
    'pages/faq.html': {
        'title': 'FAQ', 'base_path': '../', 'css_path': '../css/style.css', 'js_path': '../js/script.js',
        'content': '''<h2>FAQ</h2><p>Frequently Asked Questions.</p>'''
    }
}

for path, data in files.items():
    with open(os.path.join(project_dir, path), 'w') as f:
        f.write(html_template.format(**data))

print('HTML pages created.')
