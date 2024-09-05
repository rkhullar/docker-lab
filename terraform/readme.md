## Terraform + Terragrunt Image with ASDF
This project provides a dockerfile that can be used to build an image with specific versions of terraform and terragrunt.

### Usage
```shell
docker build --build-arg TERRAFORM_VERSION=1.8.3 --build-arg TERRAGRUNT_VERSION=0.57.12 -t test-tf .
docker run -it test-tf
```
```shell
terraform --version
terragrunt --version
```
