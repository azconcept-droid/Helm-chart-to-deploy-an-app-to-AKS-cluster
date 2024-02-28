# Deliver Small App for K8S and a Helm Chart

1. Create a simple HTTP app in the language of your choice that upon query returns the contents of the  Azure Blob Storage in JSON format.

2. Create a Dockerfile for the application.

3. Create a Helm chart to deploy the application to AKS cluster.

Considerations:

2 Take into account proper configuration of the application via the Helm chart as it requires details for the Azure Blob Storage, address etc.

- Consider adding a mechanism to validate the application’s health - To develop and deploy your application you can use the k8s cluster in part IV.

The final result of the application, its Dockerfile and its Helm chart should all be present in a single GitHub repository.