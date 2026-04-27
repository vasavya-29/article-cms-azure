# Write-up
App Deployement using Microsoft Azure

## What Is Virtual Machine
An Azure Infrastructure as a Service (IaaS) is a type of cloud computing service that provide full access to the underlying operating system of a compute resource. These can be either Windows or Linux machines, with great availability, scalability and redundancy. These require more on-going maintenance and up-keep by cloud developers.

## What Is App Service
An Azure Platform as a Service (PaaS) is a type of cloud computing service that allow developers to focus more on their apps than the underlying infrastructure i.e Azure takes care of the infrastructure. It is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It supports multiple languages and continuous deployment.


## Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Appropriate solution
The appropriate solution for deploying this web application is App Service.

### Why I choose App service
- Azure App Service brings together everything developer need to create websites, mobile backends, and web APIs for any platform or device.
- Azure App service has a built-in infrastructure maintenance, security patching, and scaling.
- Azure App service Support multiple languages, such as .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. This  app is written using one of the supported languages i.e Python
- Azure app service allows me to Quickly build, deploy, and scale my web app

### Why not Virtual Machines
- I don't want to control the underlying Operating System or install a software on the server.
- Using App service I can quickly deploy my web application without creating programming environment.
- Virtual machines behaves like a full, separate computer that I am responsible for everything: maitenance, security, update etc.

### Justification based on cost, scalability, avaliability and workflow:

- Cost: Azure App service is less expensive than Virtual Machines. It provide different plans options such as Free and Shared (preview) plans to test or deploy an app. App Services also has built-in load balancers that help save infrastructure costs.

- Scalability: Azure provides developer with the possibility to easily scale his apps either horizontally or vertically. vertical scaling automatically increases or decreases resources allocated to our App Service, such as the amount of vCPUs or RAM, by changing the App Service pricing tier. Horizontal scaling increases or decreases the number of Virtual Machine instances our App Service is running.
    - with Auto scaling App Service can automatically scale the number of instances based on a schedule or metrics like CPU, memory or HTTP queue length. 

- Availability: Global scale with high availability. Using App service I can host my app anywhere in Microsoft's global datacenter infrastructure, and the App Service SLA promises high availability.

- Workflow: Azure App service support automated deployments from GitHub, Azure DevOps, or any Git repository. With GitHub Actions for Azure web app, developer can create workflows in github repository to build, test, package, release and deploy to Azure. 

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

- Azure app service has a hardware limitations. Also is not an appropriate solution for apps which have scope to expand for future. Instead, VMs are preferred. If this app grows to a larger scale, when we have vast increase in the number of users or when more features are added to the app, I would choose a Virtual Machine.

- For advanced scaling (auto) and traffic management features, I would go for VM. this can be done easier with Azure Virtual Machine Scale Sets.

- If this application is later implemented using another programming language that is not supported by Azure app service. here, I will choose VM and create the environment for that programming language.

- Using App service, I have limited access to the host server, if I want to control the underlying OS or install a software on the server, I have to choose Virtual Machine.
