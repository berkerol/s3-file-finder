# Concepts

## Infrastructure as code

IaC is the process of provisioning and managing cloud resources through code instead of manual actions on GUI and/or CLI of cloud providers.

It has some advantages.

* It is (in general) less time consuming than doing manual actions on GUI and CLI.
* You can have a general overview of your cloud architecture just by looking at code.
* You can have an overview how your cloud architecture is evolved in time from VCS.
* It provides visibility to other members through PRs etc. This way you can also reduce risk with feedback from other members.
* It helps debugging since you can look at potential errors easily from code instead of searching through UI.
* It is repeatable so you can create another infrastructure in a short time for example for testing purposes.
* It is consistent so you are guaranteed to have the same infrastructure in every run.
* You can manage multiple cloud platforms.

If I correctly understood, alternatives are manual actions on GUI and CLI. But IaC has many advantages (as seen above) compared to those methods. You can also create files from the commands you execute on CLI but they won't work as well as IaC.

## Observability

We want to know the data on how a microservice is performing. It is difficult to understand that in a distributed environment because it consists of many components and each needs to be examined separately. Data meaning logs, metrics, traces. These 3 pillars of observability are vital for troubleshooting issues.

Logs are texts that contain information about some operations or errors. Since each microservice will have its own logs, it is hard to keep track of them separately. So we need to have a central log aggregation solution to get logs from all microservices. Then each microservice can push logs there.

Metrics are statistics about different areas of microservice like CPU, memory, disk utilization and latency, throughput of the application. Again similar to logs, since each microservice will have its own metrics, we need to keep track of all metrics in a central place. Then the metrics server can poll metrics from microservice endpoints.

Traces are data about each internal calls between microservices. Suppose that you have a slow response and your request goes through multiple microservices. In that case, each request is assigned a unique ID and tracked as it goes through again in a central place. Then you can check time of each call.

## Security

* Restrict access using IAM users and roles. Root user must not be used, instead employees and applications should have roles with least privileged policies.
* Restrict access using security groups. For each component, only allow inbound access from sources that is really needed.
* Protect data using encryption at rest and in transit for example in S3, RDS, ELB.
