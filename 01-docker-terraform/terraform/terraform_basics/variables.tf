variable "credentials" {
  description = "Project Credentials"
  default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project Name"
  default = "engaged-plasma-448516-r0"
}

variable "region" {
  description = "Project Region"
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "Bigquery Dataset Name"
  default = "demo_dataset"
}

variable "gcp_storage_bucket" {
  description = "GCP Storage Bucket Name"
  default = "engaged-plasma-448516-r0-terra-bucket"
}

variable "gcp_storage_class" {
  description = "GCP Storage Class"
  default = "STANDARD"
}