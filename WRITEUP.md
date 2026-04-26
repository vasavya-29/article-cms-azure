# Article CMS - Deployment Analysis

## VM vs App Service: Comparison

### Virtual Machine
A Virtual Machine (VM) gives full control over the operating system and environment.
The developer is responsible for setting up the web server (nginx), configuring SSL,
installing dependencies, managing OS patches, and handling scaling manually.
This approach requires significantly more setup time and ongoing maintenance.

**Pros:**
- Full control over environment and OS configuration
- Can install any software or custom runtime
- Better for complex, stateful applications

**Cons:**
- High setup complexity (SSH, nginx, ODBC drivers, SSL)
- Developer responsible for OS security and patching
- Manual scaling and availability management
- More expensive for small workloads

### App Service
Azure App Service is a fully managed platform (PaaS) that handles the underlying
infrastructure automatically. Deployment is straightforward via GitHub or zip deploy,
environment variables are managed securely in the portal, and scaling is built in.

**Pros:**
- Simple deployment directly from code or GitHub
- No server configuration required
- Built-in SSL, scaling, and monitoring
- Environment variables managed securely in portal
- Built-in log streaming for debugging
- Free F1 tier available for development

**Cons:**
- Less control over the underlying environment
- Limited to supported runtimes (Python 3.10 in this case)
- Free tier has compute limitations

## My Choice: App Service

I chose **Azure App Service** for this project for the following reasons:

1. **Simplicity** — No need to configure nginx, SSH, or SSL certificates manually.
2. **Security** — Credentials stored as environment variables, not hardcoded in files.
3. **Speed** — Deployment takes minutes compared to the extensive VM setup process.
4. **Built-in logging** — Log Stream in the portal makes it easy to capture authentication
   logs required for the project rubric.
5. **Cost** — The Free F1 tier is sufficient for this course project with no additional cost.

For a production application with custom runtime requirements or stateful workloads,
a VM would be the better choice. For this Flask-based CMS project, App Service
provides everything needed with minimal overhead.
